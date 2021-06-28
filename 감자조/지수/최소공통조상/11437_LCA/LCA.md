### 내 풀이

1. 이렇게 푼 이유?

   1. 코드1
      - 부모 정보가 필요.
      - 왼쪽, 위에 있을 수록 번호가 작은 것을 확인해서 두 정점 A,B 의 부모가 같지 않다면 둘중 번호가 큰것이 부모로 올라가게 함
      - 처음에 시간초과 나서 DP가 필요할까 해서 추가 했는데도 시간초과
        - 새로 구하려는 정점 두개를 가지고 부모로 올라가 보면서 확인하다가 공통 조상을 아는 노드가 된 경우 DP로 구함
   2. 코드2
      - 블로그 참고하여 정점의 뎁스 정보를 추가하여 구현
      - 뎁스가 동일할때까지 각자 한칸씩 올려보고, 동일해지면 그냥 하나만 갖고 위로 올라가 봄
      - 근데도 시간초과

2. 실행시간

   - python : 시간초과

3. 코드1

   ```python
   import sys
   sys.stdin = open('input.txt')
   
   N = int(input())
   p = [i for i in range(N+1)]
   DP = {}
   
   for _ in range(N-1):
       v, w = map(int, input().split())
       if v > w:
           v, w = w, v
       p[w] = v
   
   def findCommonParent(x, y):
       c_x, c_y = x, y
   
       while x != y:
           if DP.get((x, y), 0):
               return DP[(x, y)]
           if x > y:
               x = p[x]
           else:
               y = p[y]
   
       DP[(c_x, c_y)] = x
       DP[(c_y, c_x)] = x
       return x
   
   M = int(input())
   for _ in range(M):
       x, y = map(int, input().split())
       print(findCommonParent(x, y))
   ```

4. 코드2

   ```python
   import sys
   sys.stdin = open('input.txt')
   
   # p의 자식 노드들 node[p]
   # n번 노드의 뎁스 depth[n]
   
   def getSameDepth(x, y):
       if depth[x] > depth[y]: # x가 올라가야 함.
           return getSameDepth(parent[x], y)
       elif depth[y] > depth[x]: # y가 올라가야 함.
           return getSameDepth(x, parent[y])
       else: # 뎁스가 같은 경우
           return x, y
   
   def findLCA(x, y):
       while x != y:
           x = parent[x]
           y = parent[y]
       return x
   
   N = int(input())
   node = [[] for _ in range(N+1)]
   parent = [i for i in range(N+1)]
   depth = [0] * (N+1)
   
   for _ in range(N-1):
       p, c = map(int, input().split())
       if p > c:
           p, c = c, p
       node[p].append(c)
       parent[c] = p
   
   visit = [0] * (N+1)
   que = [(0, 1)]
   visit[1] = 1
   
   while que:
       deep, v = que.pop(0)
       for w in node[v]:
           if visit[w] == 0:
               depth[w] = deep + 1
               visit[w] = 1
               que.append((depth[w], w))
   
   M = int(input())
   for _ in range(M):
       x, y = map(int, input().split())
       a, b = getSameDepth(x, y)
       if a == b:
           print(a)
       else:
           print(findLCA(a, b))
   ```



### 다른 사람의 풀이1

1. 실행시간

   - 288ms (python) 

2. 코드

   ```python
   import sys
   sys.stdin = open('input.txt')
   from functools import lru_cache
   
   read = sys.stdin.readline
   sys.setrecursionlimit(10**9)
   
   n = int(read())
   graph = [[] for _ in range(n+1)]
   visited = [False] * (n+1)
   parent = [-1 for _ in range(n+1)]
   rank = [-1 for _ in range(n+1)]
   
   for _ in range(n-1):
       a, b = map(int, read().split())
       graph[a].append(b)
       graph[b].append(a)
   
   def dfs(i, r): # rank 구하기
       for node in graph[i]:
           if visited[node]:  # if visited: it's parent
               continue
           visited[node] = True
           rank[node] = r + 1
           parent[node] = i
           dfs(node, r + 1)
   
   visited[1] = True
   dfs(1, 0)
   
   @lru_cache() # 있으면 288ms / 없으면 90% 까지 가다가 시간초과
   def lcu(a, b):
       if a == b:
           return a
       if rank[a] == rank[b]:
           return lcu(parent[a], parent[b])
       if rank[b] < rank[a]:  # make a above b
           a, b = b, a
       return lcu(a, parent[b])
   
   
   m = int(read())
   for _ in range(m):
       a, b = map(int, read().split())
       print(lcu(a, b))
   ```

3. 해설

   - 뎁스(랭크) 를 구해서 랭크가 다를동안은 한쪽만 위로 올리고, 랭크가 같아지면 둘이 동시에 같이 위로 올라가면서 구하는 것.
   - 방식은 동일하며 캐싱으로 속도를 빠르게 함! [lru_cache](https://docs.python.org/ko/3/library/functools.html#functools.lru_cache)
     - 함수의 결과가 캐싱되어 저장된다. 즉 DP처럼 인자 (a, b) = ? 식으로 저장된다.





### 다른 사람의 풀이2

1. 실행시간

   - 324ms (python) 

2. 코드

   ```python
   import sys
   sys.stdin = open('input.txt')
   
   from collections import defaultdict as dd
   
   input = sys.stdin.readline
   sys.setrecursionlimit(70000)
   n = int(input())
   maxn = 65536
   connected = [[] for _ in range(n+10)]
   
   # 인접 그래프
   for _ in range(n - 1):
       a, b = map(int, input().split())
       connected[a].append(b)
       connected[b].append(a)
   
   m = int(input())
   pairset = dd(list)
   ans_order = [] # 공통조상을 구하려는 두 정점의 pk 같은 느낌
   
   for _ in range(m):
       a, b = map(int, input().split())
       pairset[a].append(b)
       pairset[b].append(a)
       ans_order.append(a * maxn + b if a < b else b * maxn + a) # 두 정점 번호로 pk? 같은 숫자를 만든다
   
   parent = {}
   visited = [False] * (n+10)
   ans = {}
   
   def find(x):
       if parent[x] == x:
           return x
       parent[x] = find(parent[x])
       return parent[x]
   
   def union(x, y):
       parent[find(y)] = find(x)
   
   def LCA(start):
       parent[start] = start # parent = {i: i for i in range(N)} 한 것과 동일
       for child in connected[start]: # 연결된 정점 중
           if child in parent: # parent에 있는 것 = 이미 앞서 한번 등장한 것 = 부모 노드 인것
               continue # 제외
           LCA(child) # 아래로 한칸 내려가기
           union(start, child)
       visited[start] = True # 내가 최초로 등장한 leaf 노드인 경우 체크 됨
       for other in pairset[start]: # start, other의 공통조상을 구하는 것임
           if visited[other]: # 위에서 parent 정보 갱신 된 것만
               k = start * maxn + other if start < other else other * maxn + start
               ans[k] = find(other)
   
   LCA(1)
   for i in ans_order:
       print(ans[i])
   
   print(ans_order, ans)
   ```

3. 해설

   - [defaultdict ](https://dongdongfather.tistory.com/69): 말 그대로 디폴트값을 지정할 수 있는 딕셔너리, 벨류를 지정하지 않았을때 가질 값을 초기에 설정 가능해서, 누적값을 구하려는 경우등에서 .get(?, ?) 등을 대체할 수 있다.
   - 풀이가 신기해서 가져왔는데 정확히 이해 되지는 않는다.
   - LCA 함수를 수행하면 가장 말단 노드들까지 일단 내려가고 방문체크한 후, 공통조상을 구하려는 정점 두개가 모두 부모정보 갱신된 상태이면 정답을 구하는?식인 것 같다.