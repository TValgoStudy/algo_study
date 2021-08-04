import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
from pprint import pprint
from collections import deque


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
virus_list = []
empty_list = []

for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            virus_list.append((i, j))
        elif arr[i][j] == 0:
            empty_list.append((i, j))

length = len(empty_list)

ans = length - 3
for i in range(length-2):
    for j in range(i+1, length-1):
        for k in range(j+1, length):
            x1, y1 = empty_list[i]
            x2, y2 = empty_list[j]
            x3, y3 = empty_list[k]
            arr_copy = [arr[i][:] for i in range(N)]
            arr_copy[x1][y1], arr_copy[x2][y2], arr_copy[x3][y3] = 1, 1, 1

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
                            # if ans < cnt:
                            #     break
                if ans < cnt:
                    break
            if ans > cnt:
                ans = cnt

print(length - ans - 3)