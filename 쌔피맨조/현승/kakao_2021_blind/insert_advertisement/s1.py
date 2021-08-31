def time_to_second(time):
    tmp = time.split(':')
    return int(tmp[0]) * 3600 + int(tmp[1]) * 60 + int(tmp[2])


def solution(play_time, adv_time, logs):
    answer = ''

    play_time_sec = time_to_second(play_time)
    time = [0 for _ in range(play_time_sec + 1)]

    for log in logs:
        tmp = log.split('-')
        start = time_to_second(tmp[0])
        end = time_to_second(tmp[1])

        time[start] += 1
        time[end] -= 1

        # time : i초에 시청중인 시청자 수
    for i in range(play_time_sec):
        time[i + 1] += time[i]

    adv_time_sec = time_to_second(adv_time)

    # 0초 ~ 광고시간 동안 총합
    # 사실 처음과 끝만 더해도 상관없다.
    viewers = time[0] + time[adv_time_sec - 1]

    i = 1
    max_idx = 0
    max_viewers = viewers
    limit = play_time_sec - adv_time_sec + 1
    while i <= limit:
        viewers -= time[i - 1]
        viewers += time[i + adv_time_sec - 1]
        if max_viewers < viewers:
            max_viewers = viewers
            max_idx = i
        i += 1

    # 문자열 형식으로 바꿔주기

    hour = max_idx // 3600
    minute = (max_idx - hour * 3600) // 60
    second = max_idx - hour * 3600 - minute * 60
    hour = str(hour) if hour > 9 else '0' + str(hour)
    minute = str(minute) if minute > 9 else '0' + str(minute)
    second = str(second) if second > 9 else '0' + str(second)
    answer = hour + ':' + minute + ':' + second
    return answer