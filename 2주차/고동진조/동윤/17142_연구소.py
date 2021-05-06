import sys
sys.stdin = open("input.txt", "r")

from itertools import combinations
from collections import deque

from itertools import combinations
from collections import deque

def bfs(Q, case):
    copy = [[grid[r][c] for c in range(N)] for r in range(N)]
    cnt = 0
    time = -1
    while Q:
        time += 1
        if cnt == total: return time
        L = len(Q)
        for _ in range(L):
            r, c = Q.popleft()
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < N and 0 <= nc < N:
                    if copy[nr][nc] == 0:
                        cnt += 1
                        copy[nr][nc] = 1
                        Q.append([nr, nc])
                    elif copy[nr][nc] == 2 and [nr, nc] not in case:
                        copy[nr][nc] = 1
                        Q.append([nr, nc])


    return -1


N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

vir = []
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]
total = 0
answer = -1
for r in range(N):
    for c in range(N):
        if grid[r][c] == 2:
            vir.append([r, c])
        elif grid[r][c] == 0:
            total += 1

for case in combinations(vir, M):
    Q = deque(list(case))
    temp = bfs(Q, case)
    if not temp == -1:
        if answer == -1:
            answer = temp
        else:
            answer = min(answer, temp)

print(answer)
