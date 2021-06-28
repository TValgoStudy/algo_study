import sys
sys.stdin = open('input.txt')

N = int(input())
graph = [[0] * (N+1) for _ in range(N+1)]

for _ in range(N-1):
    v, w = map(int, input().split())
    graph[v][w] = 1
    graph[w][v] = 1

que = [1]
p = [i for i in range(N+1)]

while que:
    v = que.pop(0)
    for w in range(1, N+1):
        if graph[v][w]:
            que.append(w)
            p[w] = v
            graph[v][w] = 0
            graph[w][v] = 0


def findCommonParent(x, y):
    while x != y:
        if x > y:
            x = p[x]
        else:
            y = p[y]
    return x


M = int(input())
for _ in range(M):
    x, y = map(int, input().split())
    print(findCommonParent(x, y))

