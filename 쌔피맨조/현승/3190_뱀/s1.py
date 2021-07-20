import sys
sys.stdin = open("input.txt", "r")
from pprint import pprint
from collections import deque

# 입력
N = int(input())
K = int(input())
arr = [[0 for _ in range(N+1)] for _ in range(N+1)]
for _ in range(K):
    r, c = map(int, input().split())
    arr[r][c] = 1
L = int(input())
x_list = [0 for _ in range(L)]
c_list = ['' for _ in range(L)]
for i in range(L):
    x, c = input().split()
    x_list[i], c_list[i] = int(x), c

# 사전 준비
arr[1][1] = 2
snakes = deque([(1, 1)])
time = 0
x, y, nx, ny = 1, 1, 1, 1
dx, dy = 0, 1
L_idx = 0
dir_list = [(0, 1), (1, 0), (0, -1), (-1, 0)]
dir_idx = 0

while True:
    time += 1
    nx += dx
    ny += dy

    if not (0 < nx <= N and 0 < ny <= N) or arr[nx][ny] == 2:
        break
    # 사과 아닌 땅인 경우 현재 꼬리 지우기
    if arr[nx][ny] == 0:
        tail_x, tail_y = snakes.popleft()
        arr[tail_x][tail_y] = 0
    arr[nx][ny] = 2
    snakes.append((nx, ny))

    # 방향 전환
    if L_idx < L and time == x_list[L_idx]:
        if c_list[L_idx] == 'D':
            dir_idx += 1
            if dir_idx == 4:
                dir_idx = 0
        else:
            dir_idx -= 1
            if dir_idx == -1:
                dir_idx = 3

        dx, dy = dir_list[dir_idx]
        L_idx += 1

print(time)