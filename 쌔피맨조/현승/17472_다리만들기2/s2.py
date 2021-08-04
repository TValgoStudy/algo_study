import sys
sys.stdin = open("input.txt", "r")
from pprint import pprint
from collections import deque

def bfs(i, j, num):
    q = deque([(i, j)])
    visited[i][j] = 1
    arr[i][j] = num
    while q:
        x, y = q.popleft()
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = 1
                arr[nx][ny] = num
                q.append((nx, ny))

#크루스칼
def find_set(x):
    while p[x] != x:
        x = p[x]
    return x

def union(x, y):
    x = find_set(x)
    y = find_set(y)
    p[x] = y

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

# 섬의 영역 표시하기 bfs
num = 0
visited = [[0 for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        if not visited[i][j] and arr[i][j]:
            num += 1
            bfs(i, j, num)

# [n1, n2, w]로 이루어진 그래프
graph = []

for x in range(N):
    region1, region2 = 0, 0
    flag = 0
    road_len = 0
    for y in range(M):
        # 섬일 때
        if arr[x][y]:
            # 첫 섬을 만남
            if flag == 0:
                flag = 1
                region1 = arr[x][y]
            # 두번째 섬을 만남
            elif flag == 2:
                if road_len > 1:
                    region2 = arr[x][y]
                    graph.append((region1, region2, road_len))
                    # 현재 섬이 첫번째섬을 만난 걸로 됨
                flag = 1
                region1 = arr[x][y]
                region2 = 0
                road_len = 0

        # 땅일 때
        else:
            # 첫 번째 섬이었다가 땅을만남 -> flag = 2
            if flag == 1:
                flag = 2
            # 첫 번재 섬을 지남 => 길갯수세기
            if flag == 2:
                road_len += 1

for y in range(M):
    region1, region2 = 0, 0
    flag = 0
    road_len = 0
    for x in range(N):
        # 섬일 때
        if arr[x][y]:
            # 첫 섬을 만남
            if flag == 0:
                flag = 1
                region1 = arr[x][y]
            # 두번째 섬을 만남
            elif flag == 2:
                if road_len > 1:
                    region2 = arr[x][y]
                    graph.append((region1, region2, road_len))
                    # 현재 섬이 첫번째섬을 만난 걸로 됨
                flag = 1
                region1 = arr[x][y]
                region2 = 0
                road_len = 0

        # 땅일 때
        else:
            # 첫 번째 섬이었다가 땅을만남 -> flag = 2
            if flag == 1:
                flag = 2
            # 첫 번재 섬을 지남 => 길갯수세기
            if flag == 2:
                road_len += 1

graph.sort(key=lambda x: x[2])

p = [i for i in range(num+1)]

total = 0
for n1, n2, w in graph:
    if find_set(n1) != find_set(n2):
        union(n1, n2)
        total += w

x = find_set(1)
for i in range(1, num+1):
    if x != find_set(i):
        total = -1
        break


print(total)