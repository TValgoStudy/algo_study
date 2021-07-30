### 내 풀이

1. 이렇게 푼 이유?

   - 힙을 이용한 다익스트라 구하는 방법.
   - 중간에 표시한 코드를 안넣고, 저걸 while의 조건에 걸었더니 완전 똑같은 코드인데 100%까지 통과하다 인덱스 에러남
   - 아래 처럼 수정하니까 통과함 무슨 차인지 모르겠음

2. 실행시간

   - 108ms (python)

3. 코드

   ```python
    # heap 사용 108ms
    import sys
    from heapq import heappush, heappop
    sys.stdin = open('input.txt')
    
    C, R = map(int, input().split())
    arr = [list(map(int, input())) for _ in range(R)]
    dist = [[99999 for _ in range(C)] for _ in range(R)]
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    
    def BFS():
        heap = [(0, 0, 0)]
        dist[0][0] = 0
    
        while heap:
            d, r, c = heappop(heap)
    
            if (r, c) == (R-1, C-1): # 💘
                return d
    
            for k in range(4):
                nr, nc = r + dr[k], c + dc[k]
                if 0 <= nr < R and 0 <= nc < C:
                    nd = arr[nr][nc] + d
                    if nd < dist[nr][nc]:
                        dist[nr][nc] = nd
                        heappush(heap, (nd, nr, nc))
    
        return dist[R-1][C-1]
    
    print(BFS())
   ```



### 다른 사람의 풀이

1. 실행시간

   - 76ms / love_adela

2. 코드

   ```python
    from sys import stdin

    m, n = map(int, input().split())
    status = stdin.read().split() 
    
    def dijkstra():
        COST = [[1e4]*m for _ in range(n)]
        COST[0][0] = 0
        deque = [(0, 0)]
    
        while True:
            x, y = deque.pop(0) 
            if x == m-1 and y == n-1:
                return COST[n-1][m-1]
    
            cost = COST[y][x]
            for x, y in [(x, y-1), (x-1, y), (x+1, y), (x, y+1)]:
                if not (0 <= x < m and 0 <= y < n):
                    continue
    
                is_wall = status[y][x] == '1'
                new_cost = cost + (1 if is_wall else 0)
    
                if COST[y][x] <= new_cost:
                    continue
    
                COST[y][x] = new_cost
                if is_wall:
                    deque.append((x, y))
                else:
                    deque.insert(0, (x, y))
    print(dijkstra())
   
3. 해설

   - 힙 대신 덱을 썼지만, 사용은 힙과 비슷하게 함
   - 최단 거리가 아니라, 최소로 벽을 부수는거라서 돌아가더라도 0번 부시는게 좋음
   - 그래서 벽이 없는 곳을 덱에 넣을때는 맨앞(0번에 insert) 하고,
   - 벽인 곳을 덱에 넣을때는 그냥 append 한다.
   - 그래서 최초로 도착지에 도착하면 바로 종료가 가능한것.