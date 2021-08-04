import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
from pprint import pprint
from collections import deque


def bfs():
    global ans
    arr_copy = [arr[i][:] for i in range(N)]
    q = deque(virus_list)
    cnt = 0
    while q:
        x, y = q.popleft()
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if arr_copy[nx][ny] == 0:
                    arr_copy[nx][ny] = 2
                    q.append((nx, ny))
                    cnt += 1
        if ans < cnt:
            break
    if ans > cnt:
        ans = cnt

def dfs(i, j, cnt):

    if j == M:
        j = 0
        i += 1
    if i == N:
        if cnt == 3:
            bfs()
        return

    if cnt == 3:
        bfs()
        return

    if arr[i][j] == 0:
        arr[i][j] = 1
        dfs(i, j+1, cnt+1)
        arr[i][j] = 0
    dfs(i, j+1, cnt)



N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
virus_list = []
length = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            virus_list.append((i, j))
        if arr[i][j] == 0:
            length += 1


ans = length - 3
dfs(0, 0, 0)

print(length - ans - 3)