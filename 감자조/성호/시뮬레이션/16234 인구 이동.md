# 16234 인구 이동



## 내 풀이(뭔가 꼬임)

```python
import sys
sys.stdin = open('input.txt')

def bfs():
    while queue:
        r, c = queue.pop(0)
        calc.append((r, c))
        visited[r][c] = 1
        # print(visited)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            # 범위 내에 있고 방문하지 않았으면
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0:
                if L <= abs(populations[r][c] - populations[nr][nc]) <= R:
                    queue.append((nr, nc))
    return calc
queue = []
N, L, R = map(int, input().split())
populations = [list(map(int, input().split())) for _ in range(N)]

visited = [[0]*N for _ in range(N)] # 방문표시를 할 visited

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

days = 0
flag = True
while flag: # 언제 끝날지 모름
    days += 1
    visited = [[0] * N for _ in range(N)]  # 방문표시를 할 visited
    for i in range(N):
        for j in range(N):
            calc = []
            if visited[i][j] == 0:
                queue.append((i, j))
                calc = bfs() # 계산할 (행, 열) 값을 가져옴
                L = len(calc)
                pop_sum = 0
                for k in range(L):
                    r, c = calc[k]
                    pop_sum += populations[r][c]
                avg = pop_sum // L
                for k in range(L):
                    r, c = calc[k]
                    populations[r][c] = avg
    visited = [[0] * N for _ in range(N)]
    queue = []
    for ii in range(N):
        for jj in range(N):
            if visited[ii][jj] == 0:
                queue.append((ii, jj))
                calc = bfs()
print(days)
```

bfs로 연합을 다 찾은 후 하나하나 더하고 평균내서 populations에 반영하기..

=> 끝내는 조건을 어떻게 설정해야 할지 몰라서 꼬임

=> 시간도 없고 머리도 복잡해서 답을 찾아봄



## 다른 사람 풀이

```python
from collections import deque
import sys
input = sys.stdin.readline
def bfs(i, j):
    q = deque()
    q.append([i, j])
    temp = []
    temp.append([i, j])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0:
                if l <= abs(s[nx][ny] - s[x][y]) <= r:
                    visit[nx][ny] = 1
                    q.append([nx, ny])
                    temp.append([nx, ny])
    return temp
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
n, l, r = map(int, input().split())
s = []
for i in range(n):
    s.append(list(map(int, input().split())))
cnt = 0
while True:
    visit = [[0] * n for i in range(n)]
    isTrue = False
    for i in range(n):
        for j in range(n):
            if visit[i][j] == 0:
                visit[i][j] = 1
                temp = bfs(i, j)
                if len(temp) > 1:
                    isTrue = True # 여기서 temp의 길이로 끝낼지 말지 판단
                    num = sum([s[x][y] for x, y in temp]) // len(temp)
                    for x, y in temp:
                        s[x][y] = num
    if not isTrue:
        break
    cnt += 1
print(cnt)
```

거의 비슷한데 temp의 len으로 종료 조건을 만들어준 점이 달랐고, 코드가 훨씬 깔끔했다. for 문을 두 번 쓴건 같지만 좀 더 간결하게 표현한 점이 멋있었다.

거기에 deque를 사용해서 시간적으로 효율을 높였고, 이와 비슷하게 내가 작성해본 결과 메모리 초과가 난 걸로 봐서는 메모리적으로도 훨씬 효과적으로 작성한 코드임을 알 수 있었다.





