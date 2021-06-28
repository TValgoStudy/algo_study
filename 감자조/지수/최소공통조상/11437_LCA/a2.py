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

def dfs(i, r):
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