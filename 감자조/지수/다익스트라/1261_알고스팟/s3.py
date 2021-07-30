# DFS 시간초과

import sys
sys.stdin = open('input.txt')

C, R = map(int, input().split())
arr = [list(map(int, list(input()))) for _ in range(R)]
visit = [[0 for _ in range(C)] for _ in range(R)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
ans = 987654321

def DFS(r, c, cnt):
    global ans

    if (r, c) == (R-1, C-1):
        ans = min(ans, cnt)
        return

    if cnt > ans:
        return

    for k in range(4):
        nr, nc = r + dr[k], c + dc[k]
        if 0 <= nr < R and 0 <= nc < C:
            if visit[nr][nc] == 0:
                visit[nr][nc] = 1
                DFS(nr, nc, cnt + arr[nr][nc])
                visit[nr][nc] = 0


DFS(0, 0, 0)
print(ans)