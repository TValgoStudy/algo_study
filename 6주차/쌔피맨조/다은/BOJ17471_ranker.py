import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame

N = int(input())
populations = list(map(int, input().split()))

G = []
for _ in range(N):
    temp = list(map(int, input().split()))
    G.append([temp[i]-1 for i in range(1, len(temp))])


def is_linked(District, Graph):
    check = [False] * N
    S = [District[0]]
    check[District[0]] = True
    link_cnt = 1

    while S:
        cur_v = S.pop(0)
        for e in Graph[cur_v]:
            if check[e] == False and e in District:
                check[e] = True
                S.append(e)
                link_cnt += 1

    if link_cnt == len(District):
        return True
    return False

min_diff = 0xffffff
# 지역구를 2등분한다-> 비트마스크로
for bit_comb in range(1, ((1 << N) >> 1)):
    D1 = []
    D2 = []
    d1_total = d2_total = 0
    for j in range(N):
        if bit_comb & (1 << j) != 0:
            D1.append(j)
            d1_total += populations[j]
        else:
            D2.append(j)
            d2_total += populations[j]

    # 나눠진 지역구가 연결되어 있는지 확인한다
    if len(D1) > 1:
        if is_linked(D1, G) == False:
            continue

    if len(D2) > 1:
        if is_linked(D2, G) == False:
            continue

    # 연결되어 있다면 인구수의 차를 계산한다
    diff = abs(d1_total - d2_total)

    if  diff < min_diff:
        min_diff = diff

if min_diff == 0xffffff:
    min_diff = -1
print(min_diff)