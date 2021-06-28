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

