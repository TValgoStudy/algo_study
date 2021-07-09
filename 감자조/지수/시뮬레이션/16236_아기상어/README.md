### 내 풀이

1. 이렇게 푼 이유?

   - 방문체크 매번 갱신 (물고기 먹으러 갈때마다)
   - 위, 왼쪽으로 정렬하여 생선 선택
   
2. 실행시간

   - 68ms

3. 코드

   ```python
   import sys
   sys.stdin = open('input.txt')
   input = sys.stdin.readline
   
   # 물고기 M마리, 상어 1마리
   # 처음 아기 상어 크기 2
   # 작은 물고기만 먹을 수 있음
   # 자신의 크기의 수만큼 먹으면 크기 +1
   
   N = int(input())
   arr = [list(map(int, input().split())) for _ in range(N)]
   
   
   def findShark(): # 초기 상어 위치 찾기
       for i in range(N):
           for j in range(N):
               if arr[i][j] == 9:
                   arr[i][j] = 0
                   return i, j
   
               
   def BFS():
       dr = [-1, 0, 1, 0]
       dc = [0, 1, 0, -1]
       r, c = findShark()
   
       que = [(r, c, 0)]
       size = 2 # 상어 크기
       canEat = set() # 먹을 수 있는 생선 위치
   
       dist = 0 # 상어~생선 최소 거리
       time = 0 # 전체 이동 시간
       eatCnt = 0 # 현재 사이즈에서 잡아먹은 생선 수
   
       visit = [[0] * N for _ in range(N)] # 이동 위치 체크
   
       while que:
           r, c, d = que.pop(0)
           visit[r][c] = 1
   
           if dist and d >= dist: # 아래에서 최소 거리가 구해진 경우(잡아먹을 생선 있는 경우)
               canEat = list(canEat) # 리스트로 변경
               canEat.sort(key = lambda x: (x[0], x[1])) # 위, 왼쪽 정렬
   
               fr, fc, d = canEat[0] # 먹을 생선
               arr[fr][fc] = 0 # 먹기
               eatCnt += 1 # 먹은 횟수 + 1
               time += d # 이동 거리(시간)
   
               if eatCnt >= size: # 성장
                   size += 1
                   eatCnt = 0
   
               # 초기화
               canEat = set()
               que = [(fr, fc, 0)]
               dist = 0
               visit = [[0] * N for _ in range(N)]
               continue
   
   
           for k in range(4): # 4방 이동
               nr, nc = r + dr[k], c + dc[k]
   
               if not (0 <= nr < N and 0 <= nc < N): # 범위 넘어갔거나
                   continue
   
               if arr[nr][nc] > size: # 갈 수 없거나
                   continue
   
               if visit[nr][nc]: # 갔던 곳은 스킵
                   continue
   
               que.append((nr, nc, d+1)) # 거리+1 해서 큐에 추가
               visit[nr][nc] = 1 # 방문 체크
   
               if 0 < arr[nr][nc] < size: # 잡아 먹을 수 있으면
                   dist = d + 1 # 최소거리에 기록 (BFS니까 가능)
                   canEat.add((nr, nc, d+1)) # 잡아먹을 후보에 추가
   
       return time
   
   print(BFS())
   ```



### 다른 사람의 풀이

1. 실행시간

   - 188ms

2. 코드

   ```python
   from sys import stdin
   input = stdin.readline
   def update(y,x):
       global shark
       sy, sx, v, l = shark
       fish_map[y][x]=0
       shark = [y,x,v+1,v+1] if l==1 else [y,x,v,l-1]
   
   def bfs():
       global shark
       sy,sx,v,_ = shark
       visited = [[0]*N for _ in range(N)]
       visited[sy][sx]=1
       queue = [(sy,sx)]
       depth = 0
       while queue:
           depth+=1
           can_eat_fishes = []
           len_q = len(queue)
           for _ in range(len_q):
               y,x= queue.pop(0)
               for nxt_y,nxt_x in ((y-1,x),(y,x-1),(y,x+1),(y+1,x)):
                   if (0<=nxt_y<N and 0<=nxt_x<N) and not visited[nxt_y][nxt_x] and fish_map[nxt_y][nxt_x]<=v:
                       visited[nxt_y][nxt_x]=1
                       if 0< fish_map[nxt_y][nxt_x] < v:
                           can_eat_fishes.append((nxt_y,nxt_x))
                       else:
                           queue.append((nxt_y, nxt_x))
           if can_eat_fishes:
               fish = sorted(can_eat_fishes)[0]
               update(*fish)    # shark, fish_map
               return depth
       return 0
   
   N = int(input())
   fish_map = [];shark = [];start_flag = False
   for y in range(N):
       row = list(map(int,input().split()))
       for x,v in enumerate(row):
           if v == 9:
               shark = [y,x,2,2] #y,x,size,life
           elif not start_flag and v!=0:
                   start_flag = (v<2)
       fish_map.append(row)
   fish_map[shark[0]][shark[1]] = 0
   time =0
   if start_flag:
       while True:
           tmp_time = bfs()
           if not tmp_time: break
           time+=tmp_time
   print(time)
   ```
   
   
   

