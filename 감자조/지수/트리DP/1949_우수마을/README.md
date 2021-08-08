### 내 풀이

1. 이렇게 푼 이유?

   - 얼리어답터문제랑 완전 똑같음
   - 근데 기억이 안나서 참고해서 풀어봄
   - 내가(부모가) 우수마을이면, 자식은 우수 마을 아님
   - 내가(부모자) 우수마을이 아니면, 자식은 우수 마을이어도 되고 / 아니어도 됨
   - 재귀가 루트부터 시작해서 리프노드까지 쭉쭉 들어감
   - 리프 노드인 경우 더 이상 재귀 함수 실행이 안되어서 함수가 끝난 후 아래로 내려옴
   - 즉, 실제 덧셈 연산이 되는 것은 리프 -> 루트 순
   
2. 실행시간

   - 124ms (python)

3. 코드1_실패(시간초과)

   ```python
    import sys
    sys.stdin = open('input.txt')
    sys.setrecursionlimit(10**9)
    
    # 584ms
    
    N = int(input())
    graph = [[] for _ in range(N + 1)]
    visited = [0] * (N+1)
    arr = [0] + list(map(int, sys.stdin.readline().split()))
    
    # n번 노드가 우수마을인 경우 / 아닌 경우 서브트리의 최대인원
    dp = [[0, 0] for __ in range(N+1)]
    
    for _ in range(N-1):
        v, w = map(int, sys.stdin.readline().split())
        graph[v].append(w)
        graph[w].append(v)
    
    
    def goodVillage(v):
        visited[v] = 1
        # dp[v][0] = 0  # 우수마을 아닌 경우 -> 주석 처리하면 584ms
        dp[v][1] = arr[v] # 우수마을인 경우
    
        for w in graph[v]:  # 연결된 노드 중에서
            if not visited[w]:  # 방문하지 않은 -> 결국 자식 노드가 됨
                goodVillage(w)
                dp[v][0] += max(dp[w][1], dp[w][0])  # 내가 우수 마을이 아니면, 자식은 우수마을이여도 되고 아니여도 되고
                dp[v][1] += dp[w][0]  # 내가 우수마을이면, 자식은 우수마을이 아님
    
    
    goodVillage(1)
    print(max(dp[1][0], dp[1][1]))
   ```


### 다른 사람의 풀이1

1. 실행시간

   - 88ms

2. 코드

   ```python
    import sys
    input=sys.stdin.readline
    sys.setrecursionlimit(10**9)
    n=int(input())
    w=[0]+[*map(int,input().split())]
    adj=[[] for _ in range(n+1)]
    for _ in range(n-1):
      u,v=map(int,input().split())
      adj[u].append(v)
      adj[v].append(u)
    visit=[0]*(n+1)
    def find_max(r):
      m1=w[r]; m2=0
      dmin=10**10; flag=0
      visit[r]=1
      for s in adj[r]:
        if visit[s]==0:
          m11,m21,m31=find_max(s)
          m1+=m31
          if m11>m21:
            flag=1; m2+=m11
          else:
            m2+=m21
            if dmin>m21-m11:
              dmin=m21-m11
      if flag: return m1,m2,m2
      else: return m1,m2-dmin,m2
    m1,m2,m3=find_max(1)
    print(max(m1,m2))
   ```
   
3. 해설

   - 가독성이 좋지는 않은데, 얼리어답터에서 가장 빨랐던 코드와 동일
   - DP 배열 필요 없이 그때그때의 최대값을 선택