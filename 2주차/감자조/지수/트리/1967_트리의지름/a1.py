import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def dfs(ind):
    global N,result,max_Node
    visited = [True]*(N+1)
    stack = []
    stack.append((ind,0))
    visited[ind] = False
    while stack:
        node, distance = stack.pop()
        if distance > result:
            result = distance
            max_Node = node
        if graph[node]:
            for next_node in graph[node]:
                if visited[next_node]:
                    visited[node] = False
                    stack.append((next_node,distance+graph[node][next_node]))


N = int(input())
graph = [{} for _ in range(N+1)]
for _ in range(N-1):
    A,B,C = map(int,input().split())
    graph[A][B] = C
    graph[B][A] = C

result = 0
max_Node = 0

dfs(1)
dfs(max_Node)
print(result)