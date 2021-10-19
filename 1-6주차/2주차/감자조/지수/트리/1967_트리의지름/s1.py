import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# input
V = int(input())
tree = [[] for _ in range(V+1)]
for _ in range(V-1):
    p, c, w = map(int, input().split())
    tree[p].append((c, w))
    tree[c].append((p, w))

# BFS
def BFS(s):
    que = [(s, 0)]
    visit = [0] * (V+1)
    visit[s] = 1

    max_d = 0 # 가장 먼 노드의 거리
    max_idx = s # 가장 먼 노드의 인덱스

    while que:
        v, vd = que.pop(0)

        if vd > max_d:
            max_d = vd
            max_idx = v

        for w, wd in tree[v]:
            if visit[w] == 0:
                que.append((w, vd+wd))
                visit[w] = 1

    return (max_d, max_idx)

# 실행
ans1, idx1 = BFS(1)
ans2, idx2 = BFS(idx1)
print(ans2)
