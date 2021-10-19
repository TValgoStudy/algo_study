import sys
sys.stdin = open("input.txt", "r")
import time
start = time.time()


import sys
from itertools import permutations
from copy import deepcopy

input = sys.stdin.readline

def rotate(info):
    r, c = (info[0] - info[2] - 1, info[1] - info[2] - 1)
    c_len = info[1] + info[2]-c
    r_len = info[0] + info[2]-r

    tmp = [[0 for _ in range(c_len)] for _ in range(r_len)]

    x, y = 0, 0
    while not tmp[x][y]:
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx = x + dx
            ny = y + dy
            while (0 <= nx < r_len and 0 <= ny < c_len) and not tmp[nx][ny]:
                tmp[nx][ny] = arr[x+r][y+c]
                x = nx
                y = ny
                nx += dx
                ny += dy
        x += 1
        y += 1

    for i in range(r_len):
        for j in range(c_len):
            if tmp[i][j]:
                arr[i+r][j+c] = tmp[i][j]


N, M, K = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(N)]
info = [list(map(int, input().split())) for _ in range(K)]
answer = 987654321

for perm in permutations(range(K), K):
    arr = deepcopy(A)
    # arr = [row[:] for row in A]
    for i in perm:
        rotate(info[i])
    # 행 최소합 구하기
    for row in arr:
        answer = min(sum(row), answer)

print(answer)




print("time: ", time.time() - start)
