import sys
from heapq import heappop, heappush
sys.stdin = open('input.txt')

# 각 나라에 번호를 메긴다. 두 정점과 놓을 수 있는 다리, 다리의 길이를 구한다.
# 상하좌우 중에 바다가 하나라도 있으며, 다리의 길이가 2 이상인 곳에 다리를 놓을 수 있다.
# 그래프를 만들고 나면 프림 방식과 동일
# 76ms

q = lambda: map(int, sys.stdin.readline().split())
n, m = q()
arr = [list(q())  for _ in range(n)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def indexing():
    idx = -1
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                BFS(i, j, idx)
                idx -= 1

    return arr, -idx-1


def BFS(i, j, idx):

    que = [(i, j)]
    arr[i][j] = idx

    while que:
        r, c = que.pop()

        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < n and 0 <= nc < m and arr[nr][nc] == 1:
                arr[nr][nc] = idx
                que.append((nr, nc))


def findBridge():
    for i in range(n):
        for j in range(m):
            if arr[i][j]:
                v = -arr[i][j]
                for k in range(4):
                    ni, nj = i + dr[k], j + dc[k]
                    t = 0
                    while 0 <= ni < n and 0 <= nj < m:
                        if arr[ni][nj] == 0:
                            ni += dr[k]
                            nj += dc[k]
                            t += 1
                        else:
                            if arr[ni][nj] == v:
                                t = 0
                            break

                    if t >= 2 and 0 <= ni < n and 0 <= nj < m:
                        w = -arr[ni][nj]
                        if graph[v][w]: # point1: 두섬을 연결하는 다리가 여러개일 수 있음
                            graph[v][w] = min(graph[v][w], t) # 그중 최소로
                        else:
                            graph[v][w] = t


def prim():
    heap = []
    heappush(heap, (0, 1))
    total = 0
    node = 0

    while node < c and heap:
        dis, v = heappop(heap)

        if visit[v]:
            continue
        visit[v] = 1

        total += dis
        node += 1

        for w in range(1, c+1):
            if graph[v][w] and visit[w] == 0:
                heappush(heap, (graph[v][w], w))


    return total if node == c else -1 # 모든 섬이 연결된 것 확인



arr, c = indexing()
graph = [[0 for _ in range(c+1)] for _ in range(c+1)]
visit = [0] * (c+1)
findBridge()
print(prim())