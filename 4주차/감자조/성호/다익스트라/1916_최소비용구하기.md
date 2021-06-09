# 1916 최소비용구하기

## 내 풀이(오답)

```python
import sys
sys.stdin = open('input.txt')

import heapq

def dijkstra(start_point):
    dist[start_point] = 0
    heap = []
    heapq.heappush(heap, (0, start_point))

    while heap:
        w, r = heapq.heappop(heap)
        for j in range(N+1):
            if cities[r][j]:
                if dist[j] > dist[r] + cities[r][j]:
                    dist[j] = dist[r] + cities[r][j]
                    heapq.heappush(heap, (dist[j], j))


N = int(input())
M = int(input())
cities = [[0 for _ in range(N+1)] for _ in range(N+1)]
for _ in range(M):
    start, end, cost = map(int, input().split())
    cities[start][end] = cost
start_point, target = map(int, input().split())
dist = [987654321]*(N+1)
dijkstra(start_point)
print(dist[target])
print(dist)
```

틀린 이유: 같은 경로에 대해 비용이 다른 여러 대의 버스가 올 수 있음을 간과함



## 수정한 코드(정답)

```python
import heapq

def dijkstra():
    heap = []
    dist[s] = 0 # s에서 s로 가는 비용은 0
    heapq.heappush(heap, (0, s))

    while heap:
        cost, start = heapq.heappop(heap)
        for j in range(1, N+1):
            if graph[start][j] > -1:
                if dist[j] > graph[start][j] + cost:
                    dist[j] = graph[start][j] + cost
                    heapq.heappush(heap, (dist[j], j))

N = int(input())
M = int(input())

graph = [[-1 for _ in range(N+1)] for _ in range(N+1)]
for _ in range(M):
    start, end, w = map(int, input().split())
    if graph[start][end] > -1:
        if graph[start][end] > w:
            graph[start][end] = w # 같은 경로를 이동하는 버스의 경우 w가 작은 것만 추가
    else:
        graph[start][end] = w
s, e = map(int, input().split()) # target start, end point
dist = [987654321] * (N+1)

dijkstra()

print(dist[e])
```

같은 경로를 이동하는 버스가 있다면 비용이 더 적은 버스를 graph에 넣어준다.



