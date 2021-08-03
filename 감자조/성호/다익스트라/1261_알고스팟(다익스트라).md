# 1261_알고스팟(다익스트라)

## 내 풀이(216ms)

다익스트라로 분류되어 있길래 다익스트라를 복습하고 풀었다.

```python
import heapq

def dijkstra():
    dist[0][0] = 0 # 0에서 0으로 가는 경우 0
    heap = []
    heapq.heappush(heap, (dist[0][0], 0, 0))

    while heap:
        w, r, c = heapq.heappop(heap) # 가중치, r, c
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < M:
                if dist[nr][nc] > dist[r][c] + int(miro[nr][nc]):
                    dist[nr][nc] = dist[r][c] + int(miro[nr][nc])
                    heapq.heappush(heap, (dist[nr][nc], nr, nc))

M, N = map(int, input().split())
miro = [input() for _ in range(N)]
# 0은 빈 방, 1은 벽
# N, M으로 이동할 때 부숴야 하는 벽의 최소 개수
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
dist = [[987654321] * M for _ in range(N)]
dijkstra()

print(dist[N-1][M-1])
```

한 번 배워놓은 알고리즘은 금방 공부해서 금방 다시 쓸 수 있다는 점이 기분 좋았다. 다익스트라를 완전히 잊어버리고 있었는데 다시 상기시켜 주는 문제였다.



## 가장 빠른 풀이(132ms)

```python
from _collections import deque

m, n = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(map(int, input())))

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def bfs():
    q = deque()
    q.append((0, 0))
    distance = [[int(1e9) for _ in range(m)] for _ in range(n)]
    distance[0][0] = 0
    visited = [[False for _ in range(m)] for _ in range(n)]
    while q:
        pop_x, pop_y = q.popleft()

        for i in range(4):
            nx, ny = pop_x + dx[i], pop_y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == False:
                if data[nx][ny] == 1:
                    distance[nx][ny] = distance[pop_x][pop_y] + 1
                    q.append((nx, ny))
                else:
                    distance[nx][ny] = distance[pop_x][pop_y]
                    q.appendleft((nx, ny))
                visited[nx][ny] = True
    print(distance[n - 1][m - 1])


bfs()
```

다익스트라와 형태는 같아 보이지만 bfs로, 방문 표시를 해서 재방문을 하지 않고, deque를 사용해서 pop(0)로 발생할 수 있는 시간 지연을 방지했다.

방문 표시 덕분에 다익스트라보다 더 빠른 것 같다. 