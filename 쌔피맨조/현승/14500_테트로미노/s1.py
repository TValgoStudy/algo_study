import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
from pprint import pprint
N, M = map(int, input().split())
# bfs로는 힘들다!!!
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for i in range(N):
    for j in range(M):

        visited = [[0 for _ in range(7)] for _ in range(7)]
        que = deque([(i, j)])

        visited[3][3] = arr[i][j]
        p, q = 3 - i, 3 - j
        cnt = -1
        while q:
            cnt += 1
            if cnt == 3:
                break
            for _ in range(len(que)):
                x, y = que.popleft()
                for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    nx, ny = x + dx, y + dy
                    if abs(nx - i) + abs(ny - j) != cnt + 1:
                        continue
                    if 0 <= nx < N and 0 <= ny < M:
                        if visited[p + nx][q + ny] < arr[nx][ny] + visited[p + x][q + y]:
                            visited[p + nx][q + ny] = arr[nx][ny] + visited[p + x][q + y]
                            que.append((nx, ny))

                            if cnt == 2:
                                if ans < visited[p + nx][q + ny]:
                                    ans = visited[p + nx][q + ny]
        pprint(visited)
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            x, y = i + dx * 2, j + dy * 2
            if 0 <= x < N and 0 <= y < M:
                max_val = 0
                if 0 <= i+dx+dy < N and 0 <= j+dy+dx < M and max_val < arr[i+dx+dy][j+dy+dx]:
                    max_val = arr[i+dx+dy][j+dy+dx]
                if 0 <= i+dx-dy < N and 0 <= j+dy-dx < M and max_val < arr[i+dx-dy][j+dy-dx]:
                    max_val = arr[i+dx-dy][j+dy-dx]
                if ans < visited[p + x][q + y] + max_val:
                    ans = visited[p + x][q + y] + max_val


print(ans)