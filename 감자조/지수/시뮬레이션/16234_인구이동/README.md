### 내 풀이

1. 이렇게 푼 이유?

   - 방문체크 매번 갱신 새로운 턴을 탐색할 때 마다
   - BFS로 연합인 마을 리스트 구성
   - 모든 마을을 탐색한 후 연합마을이 있으면, 엽합된 마을들 인구수 조정
   - 연합 없을때까지 반복
   
2. 실행시간

   - python 7812ms / pypy 1160ms

3. 코드

   ```python
    # python 7812ms
    # pypy 1160ms
    
    
    import sys
    sys.stdin = open('input.txt')
    q = lambda : map(int, sys.stdin.readline().split())
    
    
    def solution():
        global visit
    
        cnt = 0 # 인구이동 횟수
    
        while True:
            visit = [[0 for _ in range(N)] for __ in range(N)] # 초기화
            linked = [] # 초기화
    
            for r in range(N):
                for c in range(N):
                    if visit[r][c]: continue # 방문한 마을 스킵
    
                    ans = BFS(r, c) # 방문하지 않은 마을 BFS로 인접 마을 확인
    
                    if ans: # 연합이 있으면
                        linked.append(ans) # 연합 결과 기록
    
            if not linked: break # 아무 연합도 없으면 반복 종료
    
            cnt += 1
    
            for val, group in linked:
                for i, j in group:
                    arr[i][j] = val # 연합 결과로 인구수 n빵
    
        return cnt
    
    
    
    def BFS(r, c):
        global visit
    
        que = [(r, c)]
        group = [(r, c)] # 연합 마을
        val = arr[r][c] # 연합 마을 총 인원수
        visit[r][c] = 1
        link = 1 # 연합된 마을 수
    
        while que:
            r, c = que.pop()
            for k in range(4):
                nr, nc = r + dr[k], c + dc[k]
                if 0 <= nr < N and 0 <= nc < N: # 범위체크
                    if visit[nr][nc] == 0: # 방문체크
                        if L <= abs(arr[r][c] - arr[nr][nc]) <= R: # 조건체크
                            link += 1
                            que.append((nr, nc))
                            group.append((nr, nc))
                            val += arr[nr][nc]
                            visit[nr][nc] = 1
    
        if link > 1:
            return [val // link , group]
        else:
            return 0
    
    
    
    N, L, R = q()
    arr = [list(q()) for _ in range(N)]
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    visit = [[0 for _ in range(N)] for __ in range(N)]
    
    print(solution())
   ```



### 다른 사람의 풀이

1. 실행시간

   - 368ms / 1sss123ss

2. 코드

   ```python
    import sys
    from collections import deque
    
    def bfs(i,j,visited,ans):
        q=deque()
        union=[(i,j)]
        q.appendleft((i,j))
        visited[i][j]=ans
        cnt=1
        population=country[i][j]
    
        while q:
            x,y=q.pop()
    
            for d in dir:
                nx,ny=x+d[0],y+d[1]
                if 0<= nx < N and 0<= ny <N:
                    if visited[nx][ny] != ans and L <= abs(country[nx][ny] - country[x][y]) <= R:
                        visited[nx][ny]=ans
                        q.appendleft((nx,ny))
                        union.append((nx,ny))
                        cnt+=1
                        population+=country[nx][ny]
    
        # 인구 이동
        if cnt>1:
            pop_mean=population//cnt
            for x,y in union:
                country[x][y]=pop_mean
                search.appendleft((x,y))
            return True
        return False
    
    N,L,R=map(int,sys.stdin.readline().split())
    dir=[(1,0),(-1,0),(0,1),(0,-1)]
    country=[]
    for _ in range(N):
        country.append(list(map(int,sys.stdin.readline().split())))
    
    search=deque()
    for i in range(N):
        for j in range(N):
            search.appendleft((i,j))
    
    visited=[[-1]*N for _ in range(N)]
    def solution():
        ans=0
        while True:
            stop=True
            for _ in range(len(search)):
                i,j=search.pop()
                if visited[i][j]!=ans:
                    if bfs(i,j,visited,ans):
                        stop =False
            if stop:
                break
            ans+=1
        print(ans)
    
    solution()
   ```
  
3. 해설

   - 비슷한 방법인데 visit를 매번 초기화하지 않고 사용
   
   

