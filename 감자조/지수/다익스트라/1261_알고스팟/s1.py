# BFS 시간초과

import sys
sys.stdin = open('input.txt')

C, R = map(int, input().split())
arr = [list(map(int, list(input()))) for _ in range(R)]
dist = [[99999 for _ in range(C)] for _ in range(R)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def BFS():
    que = [(0, 0, 0)]

    while que:
        r, c, d = que.pop(0)
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < R and 0 <= nc < C:
                nd = arr[nr][nc] + d
                if nd < dist[nr][nc]:
                    dist[nr][nc] = nd
                    que.append((nr, nc, arr[nr][nc] + d))

    return dist[R-1][C-1]

print(BFS())