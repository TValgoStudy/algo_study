### 내 풀이

1. 이렇게 푼 이유?

   - MST를 풀려면 정점과 정점사이의 거리를 알아야하는데, 이걸 직접 구하는게 중요했던 문제
   - 방향델타로 거리는 쉽게 구할 수 있지만, 놓아진 다리의 양끝이 `몇번째 섬`인지를 먼저 알아야 함
     - 정점 번호를 모르면, n-1개의 정점이 연결 완료된지를 알수 없음
     - 방문체크도 할 수 없음
   - 그래서 먼저 1들이 연속해서 나온 뭉쳐져있는 덩어리의 섬을 찾고 먼저 찾는것부터 라벨링 함
     - 다 1로 되어 있어서 먼저 발견되는것부터 -1 ~ -n으로 지정
   - 모든 좌표를 탐색하면서 길이가 2이상의 다리를 놓을 수 있는지 체크, 다리가 놓아지면 정점과, 다리길이를 graph에 저장
   - 섬을 연결하는 다리가 여러개일 수 있어서 가장 작은 것을 택함
   - 그래프가 다 구해지면 프림과 동일, 마지막에 노드를 다 연결하거나 힙이 empty전까지 반복한다
   - 연결한 노드수와 정점수가 같으면 total을 아니면 -1을 출력

2. 실행시간

   - 72ms

3. 코드

   ```python
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
   ```



### 다른 사람의 풀이

1. 실행시간

   - 56ms / [dbsdlswp](https://www.acmicpc.net/source/15348963)

2. 코드

   ```python
    # https://www.acmicpc.net/problem/17472
    
    def dfs(r,c,idx):
        for dr, dc in dir:
            rr = r + dr
            cc = c + dc
            if 0 <= rr and rr < R and 0 <= cc and cc < C:    
                if arr[rr][cc] == 1:
                    arr[rr][cc] = idx
                    dfs(rr,cc,idx)
    
    def bfs(idx):
        que = []
        for r in range(R):
            for c in range(C):
                if arr[r][c] == idx:
                    for d in range(4):
                        rr = r + dir[d][0]
                        cc = c + dir[d][1]
                        if 0 <= rr and rr < R and 0 <= cc and cc < C:
                            que.append([rr,cc, d])
        count = 0
        while que:
            que_ = []
    
            for r,c,d in que:
                rr = r + dir[d][0]
                cc = c + dir[d][1]
                if arr[r][c] == 0:
                    if 0 <= rr and rr < R and 0 <= cc and cc < C:
                        que_.append([rr,cc,d])
                else:
                    if arr[r][c] == idx:
                        continue
                    if count < 2:
                        continue
                    if inner[idx][arr[r][c]] == 0:
                        inner[idx][arr[r][c]] = count
    
            que = que_
            count += 1
    
    
    dir = [[-1,0], [1,0], [0,-1], [0,1]]
    R, C = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(R)]
    
    idx = 2
    for r in range(R):
        for c in range(C):
            if arr[r][c] == 1:
                arr[r][c] = idx
                dfs(r,c, idx)
                idx += 1
    
    inner = [[0] * idx for _ in range(idx)]
    
    for i in range(2,idx):
        bfs(i)
    
    brr = []
    
    for r in range(2,idx):
        for c in range(r+1,idx):
            if inner[r][c] == 0:
                continue
            brr.append([r,c,inner[r][c]])
    
    brr = sorted(brr, key= lambda x: x[2])
    
    crr = []
    visit = [-1] * idx
    answer = 0
    
    for a, b, v in brr:
    
        va = visit[a]
        vb = visit[b]
        if va == -1 and vb == -1:
            visit[a] = len(crr)
            visit[b] = len(crr)
            crr.append([a,b])
        elif va == -1:       # va 만 0
            visit[a] = vb
            crr[vb].append(a)
        elif vb == -1:       # vb 만 0
            visit[b] = va
            crr[va].append(b)
        else:
            if va == vb:
                continue
            else:
                if va < vb: # vb > va
                    for b_ in crr[vb]:
                        visit[b_] = va
                    crr[va] += crr[vb]
                    crr[vb] = []
                else:   # va > vb
                    for a_ in crr[va]:
                        visit[a_] = vb
                    crr[vb] += crr[va]
                    crr[va] = []
        answer += v
    
    if crr:
        if len(crr[0]) != idx-2:
            print('-1')
        else:
            print(answer)
    else:
        print('-1')

3. 해설

   - dfs는 섬에 번호를 매기는 역할, bfs는 섬간 거리를 구하는 역할로 사용됨