import sys
sys.stdin = open('input.txt')
input = lambda : sys.stdin.readline()
sys.setrecursionlimit(10**6)

from functools import cache

from collections import defaultdict
graph = defaultdict(list)
n = int(input())
depth = [0]*(n+1)
depth[1] = 1
for i in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [0]*(n+1)
def dfs(node, dpts):
    for next_node in graph[node]:
        if depth[next_node] == 0:
            depth[next_node] = dpts
            parent[next_node] = node
            dfs(next_node, dpts+1)

@cache
def lca(a, b):
    if depth[a] > depth[b]:
        a, b = b, a

    while depth[b] != depth[a]:
        b = parent[b]

    while a != b:
        a, b = parent[a], parent[b]

    return a

dfs(1, 2)

m = int(input())

for i in range(m):
    a, b = map(int, input().split())
    print(lca(a,b))