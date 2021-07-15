### 내 풀이

1. 이렇게 푼 이유?

   - 설마 조합을 다 봐야하나 했는데 진짜 그랬다
   - 조합 + BFS

2. 실행시간

   - 3016ms(pypy) ; python3는 시간초과

3. 코드

   ```python
    import sys
    import copy
    
    # 3016ms pypy
    sys.stdin = open('input.txt')
    
    
    
    def getArea(): # 초기값 구하기
        safe = 0 # 안전지대의 수
        virus = [] # 바이러스의 위치
        for i in range(N):
            for j in range(M):
                if arr[i][j] == 0:
                    safe += 1
                if arr[i][j] == 2:
                    virus.append((i, j))
        return safe, virus
    
    
    def BFS(): # 바이러스 퍼트리기
        global MIN
        
        wall = copy.deepcopy(arr) # 2차원 배열 복사
        que = list(virus) # 바이러스로 큐 초기화
        cnt = 0 # 바이러스가 퍼진 빈칸 수
    
        while que:
            if cnt > MIN: # 백트래킹 : 최소보다 커지면 그만
                return
    
            r, c = que.pop(0)
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < N and 0 <= nc < M:
                    if wall[nr][nc] == 0:
                        cnt += 1
                        wall[nr][nc] = 2
                        que.append([nr, nc])
    
        MIN = min(MIN, cnt)
    
    
    def setWall(idx): # 벽 3개 모든 조합
        if idx == 3:
            BFS()
            return
        for i in range(N):
            for j in range(M):
                if arr[i][j] == 0:
                    arr[i][j] = 1
                    setWall(idx+1)
                    arr[i][j] = 0
    
    N, M = map(int, sys.stdin.readline().split())
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    MIN = 100
    
    safe, virus = getArea()
    setWall(0)
    print(safe - MIN - 3)
   ```



### 다른 사람의 풀이

1. 실행시간

   - 276ms

2. 코드

   ```python
    import sys
    from itertools import combinations
    
    sys.stdin = open('input.txt')
    
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for ARR in range(N)]
    cnt_max = 0
    
    
    def blocking(list):
        global virus_max
        arr_new = [i[:] for i in arr]
        for i in list:
            a = i // 8
            b = i % 8
            arr_new[a][b] = 1
        virus2 = virus[:]
        cnt = 0
        cntt = dfs(arr_new, virus2, cnt)
    
        if cntt < virus_max:
            virus_max = cntt
    
    
    def dfs(arr_new, vir, cnt):
        global virus_max
        while vir:
            z = vir.pop()
            node_y = z // 8
            node_x = z % 8
            if virus_max <= cnt:
                return 64
            for i in range(4):
                ny = node_y + dy[i]
                nx = node_x + dx[i]
                if 0 <= nx < M and 0 <= ny < N and arr_new[ny][nx] == 0:
                    vir.append(ny * 8 + nx)
                    arr_new[ny][nx] = 2
                    cnt += 1
    
        return cnt
    
    
    # 벽을 세울 수 있는 후보군 찾기
    possible_block = []
    virus = []
    safe_zone = 0
    virus_max = 64
    for y in range(N):
        for x in range(M):
            if arr[y][x] == 0:
                possible_block.append(y * 8 + x)
                safe_zone += 1
            elif arr[y][x] == 2:
                virus.append(y * 8 + x)
    block_3_list = combinations(possible_block, 3)
    
    for i in block_3_list:
        blocking(i)
    
    print(safe_zone - virus_max - 3)

3. 해설

   - 코드나 방식은 동일
   - 배열 최대 크기가 8이라서 최대 64로 정해둔 것
   - itertools로 조합을 구한게 더 빠름! 웬만하면(못쓰게 하는거 아니면) 라이브러리 쓰기!