# 11437_LCA



## Lowest Common Ancestor 알고리즘

https://www.youtube.com/watch?v=O895NbxirM8&t=3s

1. 모든 노드에 대해 깊이(depth)를 계산한다.
2. 최소 공통 조상을 찾을 두 노드를 확인한다.
   1. 먼저 두 노드의 깊이가 동일하도록 거슬러 올라간다.
   2. 이후에 부모가 같아질 때까지 반복적으로 두 노드의 부모 방향으로 거슬러 올라간다. 
3. 모든 LCA(a, b)연산에 대하여 2번의 과정을 반복한다.



1780ms 풀이(O(MN) 풀이)

```python
import sys
n = int(input())
sys.setrecursionlimit(int(1e5)) # 이거 안써주면 런타임 에러(재귀 깊이)
parent = [0] * (n+1) # 부모 노드 정보
d = [0] * (n+1) # 각 노드까지의 깊이
c = [0] * (n+1) # 각 노드의 깊이가 계산되었는지 여부
graph = [[] for _ in range(n+1)] # 그래프 정보

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 깊이 구하기
def dfs(x, depth):
    c[x] = True
    d[x] = depth
    for y in graph[x]: # 처음엔 2, 3
        if c[y]: # y의 깊이를 구했는지 확인
            continue # 구했으면 넘어가기
        parent[y] = x
        dfs(y, depth+1)

# a와 b의 공통 조상 찾기
def lca(a, b):
    while d[a] != d[b]: # 두 노드의 깊이가 같지 않을 때
        if d[a] > d[b]: # a의 깊이가 더 깊다면
            a = parent[a] # a의 위치를 한 칸 위로(부모로)
        else:
            b = parent[b] # b가 더 깊으면 b를 부모 노드로
    # 위의 while문을 거치면 동일 깊이에 두 노드가 위치한다.

    while a != b: # 두 노드가 같아질 때까지
        a = parent[a]
        b = parent[b]
    return a

dfs(1, 0)

m = int(input())

for i in range(m):
    a, b = map(int, input().split())
    print(lca(a, b))
```



다른 사람 풀이

from collections import defaultdict 적용

stdin.readline 적용



11438번 문제는 이렇게 풀면 시간초과가 난다고 합니다. O(logN) 풀이도 영상에서 소개하고 있으니 조만간 트리를 한번 날잡고 공부하면서 풀어보려고 합니다.