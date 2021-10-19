# brute force Max: N=50*8! =  2016000 = 10 ** 6
from itertools import permutations
N = int(input())
# Batting_forecast = [list(map(int, input().split())) for _ in range(N)]


def solution(batters, now_batter):
    out_count = 0
    score = 0
    # 1루, 2루, 3루
    status = [0, 0, 0]
    while out_count < 3:
        if batters[now_batter] == 0:
            out_count += 1
        elif batters[now_batter] == 1:
            score += status[2]
            status = [1, status[0], status[1]]
        elif batters[now_batter] == 2:
            score += status[1] + status[2]
            status = [0, 1, status[0]]
        elif batters[now_batter] == 3:
            score += sum(status)
            status = [0, 0, 1]
        else:
            score += 1 + sum(status)
            status = [0, 0, 0]
        now_batter = (now_batter + 1) % 9

    return score, now_batter


# greedy 순번은 한 번 정해지면 안바뀜
# 매 이닝마다 다른 순서가 아니라 배트 순서는 동일함
aswer = 0
now_batter = 0
for _ in range(N):
    inning_max_score = 0
    batting_forecast = list(map(int, input().split()))
    temps = permutations(batting_forecast[1:], len(batting_forecast)-1)
    for temp in temps:
        batters = [batter for batter in temp]
        batters.insert(3, batting_forecast[0])
        score, new_batter = solution(batters, now_batter)
        if score > inning_max_score:
            inning_max_score = score
            renew_batter = new_batter
    now_batter = renew_batter
    answer += inning_max_score
print(answer)
