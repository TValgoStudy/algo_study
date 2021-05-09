import sys

sys.stdin = open("input.txt", "r")

from collections import deque

def bfs(first, second, d):
    v = [[[0]*3 for _ in range(N)] for _ in range(N)]
    direction_dict = {
        # 가로
        0: [(1, 1, 2), (0, 1, 0)],
        # 세로
        1: [(1, 1, 2), (1, 0, 1)],
        # 대각선
        2: [(1, 1, 2), (1, 0, 1), (0, 1, 0)]
    }
    q = deque()
    q.append((first, second, d, 1))
    v[0][1][0] = 1
    ret = 0
    while q:
        _, coor, d, cnt = q.popleft()
        x, y = coor
        if (x, y) == (N-1, N-1):
            ret += 1
        for dx, dy, d in direction_dict[d]:
            nx = x + dx
            ny = y + dy
            if not (0 <= nx < N and 0 <= ny < N):
                continue
            if arr[nx][ny] == 1:
                continue
            if (dx, dy) == (1, 1):
                if arr[nx - 1][ny] == 1 or arr[nx][ny - 1] == 1:
                    continue

            q.append(((x, y), (nx, ny), d, cnt))

    return ret

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

print(bfs((0, 0), (0, 1), 0))