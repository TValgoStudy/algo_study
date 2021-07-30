# heap 사용 100% 까지 맞다가 인덱스에러??

import sys
from heapq import heappush, heappop
sys.stdin = open('input.txt')

C, R = map(int, input().split())
arr = [list(map(int, list(input()))) for _ in range(R)]
dist = [[99999 for _ in range(C)] for _ in range(R)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def BFS():
    heap = [(0, 0, 0)]

    while dist[R-1][C-1] == 99999:
        d, r, c = heappop(heap)
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < R and 0 <= nc < C:
                nd = arr[nr][nc] + d
                if nd < dist[nr][nc]:
                    dist[nr][nc] = nd
                    heappush(heap, (nd, nr, nc))

    return dist[R-1][C-1]

print(BFS())