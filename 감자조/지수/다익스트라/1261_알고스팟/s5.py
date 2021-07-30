# heap 사용 108ms

import sys
from heapq import heappush, heappop
sys.stdin = open('input.txt')

C, R = map(int, input().split())
arr = [list(map(int, input())) for _ in range(R)]
dist = [[99999 for _ in range(C)] for _ in range(R)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def BFS():
    heap = [(0, 0, 0)]
    dist[0][0] = 0

    while heap:
        d, r, c = heappop(heap)

        if (r, c) == (R-1, C-1): # 이거 넣었다고 통과됨
            return d

        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < R and 0 <= nc < C:
                nd = arr[nr][nc] + d
                if nd < dist[nr][nc]:
                    dist[nr][nc] = nd
                    heappush(heap, (nd, nr, nc))

    return dist[R-1][C-1]

print(BFS())