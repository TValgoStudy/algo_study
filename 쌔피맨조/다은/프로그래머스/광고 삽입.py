def to_min(t: str) -> int:
    return int(t[0:2]) * 3600 + int(t[3:5]) * 60 + int(t[6:8])

def to_hms(t: int) -> str:
    h = str(t // 3600)
    m = str((t % 3600) // 60)
    s = str(((t % 3600) % 60))
    if int(h) < 10:
        h = "0" + h
    if int(m) < 10:
        m = "0" + m
    if int(s) < 10:
        s = "0" + s
    return "{}:{}:{}".format(h, m, s)


def solution(play_time, adv_time, logs):
    pyt_min = to_min(play_time)
    adt_min = to_min(adv_time)

    logs_onoff = []
    for log in logs:
        s, f = log.split('-')
        s2min, f2min = to_min(s), to_min(f)
        logs_onoff.extend([(s2min, 1), (f2min, 0)])
    logs_onoff.sort()

    if logs_onoff[-1][0] - logs_onoff[0][0] < adt_min:
        return "00:00:00"

    now_playing_list = []
    if logs_onoff[0][0] != 0: now_playing_list.append((0, 0))
    if logs_onoff[-1][0] != pyt_min: now_playing_list.append((pyt_min, 0))
    now_playing = 0
    for time, onoff in logs_onoff:
        now_playing += 1 if onoff else -1
        now_playing_list.append((time, now_playing))

    max_acc_time = 0
    result_start = 0
    for k in range(len(now_playing_list) - 1):
        t = now_playing_list[k + 1][0] - now_playing_list[k][0]
        p = now_playing_list[k][1]
        acc_time = 0
        adt_acc = 0
        kk = k
        while adt_acc + t <= adt_min:
            adt_acc += t
            acc_time += t * p
            kk += 1
            if kk + 1 < len(now_playing_list):
                t = now_playing_list[kk + 1][0] - now_playing_list[kk][0]
                p = now_playing_list[kk][1]
            else:
                break
        else:
            if adt_min > adt_acc:
                acc_time += (adt_min - adt_acc) * p
            if max_acc_time < acc_time:
                max_acc_time = acc_time
                result_start = now_playing_list[k][0]

    result = to_hms(result_start)
    return result

play_time = "50:00:00"
adv_time = "50:00:00"
logs = ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]

print(solution(play_time, adv_time, logs))
