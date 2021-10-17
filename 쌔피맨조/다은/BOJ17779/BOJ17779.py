import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def divide(d1, d2, x, y):
    section = [[0] * (N + 2) for _ in range(N + 2)]

    # 다른 선거구 세기
    # 1번 선거구: 1 ≤ r < x+d1, 1 ≤ c ≤ y
    for r in range(1, x + d1):
        for c in range(1, y + 1):
            section[r][c] = 1

    # 2번 선거구: 1 ≤ r ≤ x+d2, y < c ≤ N
    for r in range(1, x + d2 + 1):
        for c in range(y + 1, N + 1):
            section[r][c] = 2

    # 3번 선거구: x+d1 ≤ r ≤ N, 1 ≤ c < y-d1+d2
    for r in range(x + d1, N + 1):
        for c in range(1, y - d1 + d2):
            section[r][c] = 3

    # 4번 선거구: x+d2 < r ≤ N, y-d1+d2 ≤ c ≤ N
    for r in range(x + d2 + 1, N + 1):
        for c in range(y - d1 + d2, N + 1):
            section[r][c] = 4

    # 5번 선거구 경계 만들기
    # 경계 1: (x, y), (x+1, y-1), ..., (x+d1, y-d1)
    # 경계 4: (x+d2, y+d2), (x+d2+1, y+d2-1), ..., (x+d2+d1, y+d2-d1)
    for d in range(d1+1):
        if 1 <= x+d < N+1 and 1 <= y-d < N+1:
            section[x+d][y-d] = 5
        if 1 <= x+d2+d < N+1 and 1 <= y+d2-d < N+1:
            section[x+d2+d][y+d2-d] = 5

    # 경계 2: (x, y), (x+1, y+1), ..., (x+d2, y+d2)
    # 경계 3: (x+d1, y-d1), (x+d1+1, y-d1+1), ... (x+d1+d2, y-d1+d2)
    for d in range(d2+1):
        if 1 <= x+d < N+1 and 1 <= y+d < N+1:
            section[x+d][y+d] = 5
        if 1 <= x+d1+d < N+1 and 1 <= y-d1+d < N+1:
            section[x+d1+d][y-d1+d] = 5

    # 경계 사이 구역 5 채우기
    for r in range(1, N+1):
        if 5 not in section[r]:
            continue
        start = section[r].index(5)
        end = N - section[r][::-1].index(5) + 1
        if start == end:
            continue
        for c in range(start, end+1):
            section[r][c] = 5

    # 선거구 값 세기
    count = [0] * 6
    for r in range(1, N+1):
        for c in range(1, N+1):
            s = section[r][c]
            count[s] += IN[r][c]

    return max(count[1:]) - min(count[1:])


N = int(input())
IN = [[0]*(N+2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(N)] + [[0] * (N+2)]

result = 9999999
for d1 in range(1, N):
    for d2 in range(1, N):
        for x in range(1, N-d1-d2+1):
            for y in range(1+d1, N-d2+1):
                result = min(result, divide(d1, d2, x, y))
print(result)
