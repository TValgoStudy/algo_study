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