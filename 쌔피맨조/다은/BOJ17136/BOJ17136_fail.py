import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame


N = 10

# 오른쪽 아래 대각선
drc = [(0, 1), (1, 0), (1, 1)]

def expand(IN, r, c):
    global max_tmp, max_num

    if not max_tmp:
        max_tmp = [(r, c)]

    q = [(r, c)]
    num = 1
    while len(q) == 2 * num - 1:
        tmp = []
        while q:
            r, c = q.pop()
            for dr, dc in drc:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < N and 0 <= nc < N:
                    if IN[nr][nc] == 1:
                        tmp.append((nr, nc))
                        IN[nr][nc] = IN[r][c] + 1
                        num = IN[nr][nc]
        if len(tmp) == 2 * num - 1:
            q = tmp
            if len(tmp) > len(max_tmp):
                max_tmp = tmp[:]
                max_num = num
        else:
            break
    return num



IN = [list(map(int, input().split())) for _ in range(10)]

target_cnt = 0
for r in range(10):
    for c in range(10):
        if IN[r][c] == 1:
            target_cnt += 1


card = {1: 5, 2: 5, 3: 5, 4: 5, 5: 5}
result_cnt = 0
result = 0
while target_cnt:
    max_tmp , max_num = [], 1
    for r in range(N):
        for c in range(N):
            if IN[r][c] == 1:
                copy_IN = [i[:] for i in IN]
                expand(copy_IN, r, c)


    if max_num <= 5:
        card[max_num] -= 1
        r, c = max(max_tmp)
        for i in range(max_num):
            for j in range(max_num):
                IN[r - i][c - j] = '-'
        result_cnt += max_num ** 2
        result += 1

    elif max_num == 6 or max_num == 8 or max_num == 10:
        card[max_num//2] -= 2
        r, c = max(max_tmp)
        for i in range(max_num):
            for j in range(max_num):
                IN[r - i][c - j] = '-'
        result_cnt += max_num ** 2
        result += 4

    elif max_num == 7 or max_num == 9:
        card[max_num//2] -= 2
        r, c = max(max_tmp)
        for i in range(max_num-1):
            for j in range(max_num-1):
                IN[r - i][c - j] = '-'
        result_cnt += (max_num-1) ** 2
        result += 4

    flag = 0
    card_check = True
    for key, val in card.items():
        if val < 0:
            print(-1)
            flag = 1
            break
    if flag:
        break

    if card_check and target_cnt == result_cnt:
        print(result)
        break
else:
    print(0)

import datetime as dt

today = dt.datetime.now()
year = today.year
# Js에서 getMonth는 0~11이라 맞추기 위해서 -1 해줌
month = today.month - 1

days_dict = {
    0: 31, 2: 31, 4: 31, 6: 31, 7:31, 9: 31, 11: 31,
    3: 30, 5: 30, 8: 30, 10: 30,
    1:  29 if ((year % 4 == 0) and (year % 100 != 0) or (year % 400) == 0) else 28
}

days = days_dict[month]
print("{} days for {}-{}".format(days, year, month+1))
