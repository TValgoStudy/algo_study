# 다리만들기 2

import sys
sys.stdin = open("input2.txt", "r")
from pandas import DataFrame



dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
def bfs(s: tuple, check: int) -> int:
    q = [s]
    IN[s[0]][s[1]] = check
    while q:
        r, c = q.pop(0)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and IN[nr][nc] == 1:
                IN[nr][nc] = check
                q.append((nr, nc))
    return check + 1

def make_G(IN: list):
    for r in range(len(IN)):
        a, b, bridge = 0, 0, 0
        for c in range(len(IN[0])):
            # a(from 섬) 이 정해져있으면
            if a:
                # 바다면 다리 +1
                if not IN[r][c]:
                    bridge += 1
                # 섬 + a와는 다른 섬일 때
                elif IN[r][c] and a != IN[r][c]:
                    # b(to 섬) 을 정한다.
                    b = IN[r][c]
                    # 인접 행렬에 값이 있으면 비교
                    if G[a][b]:
                        if bridge > 1 and G[a][b] > bridge:
                            G[a][b] = bridge
                            G[b][a] = bridge
                    # 없으면 그냥 넣기, 단 1이상일 때
                    elif bridge > 1:
                        G[a][b] = bridge
                        G[b][a] = bridge
                    a, b, bridge = b, 0, 0
                # 섬 + a와 같은 섬일 때 다리 길이 리셋
                # 이 부분을 안해줘서 틀렸었다 !!!!!!!!!
                elif IN[r][c] and a == IN[r][c]:
                    bridge = 0

            # a가 0이면 갱신(섬이면 숫자, 바다면 0)
            else:
                a = IN[r][c]


def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]

def union(x, y):
    p[find(y)] = find(x)

def kruskal():
    G_list = []
    for r in range(2, check):
        for c in range(r, check):
            if G[r][c]:
               G_list.append((r-2, c-2, G[r][c]))
    G_list.sort(key = lambda x: x[2])


    visited = [1] * V
    edge_cnt = 0
    mst_w = 0
    while edge_cnt != E:
        if not G_list:
            return -1
        a, b, w = G_list.pop(0)
        if find(a) != find(b):
            union(a, b)
            edge_cnt += 1
            mst_w += w
            visited[a] = 0
            visited[b] = 0
    return mst_w if not sum(visited) else -1



N, M = map(int, input().split())
IN = [list(map(int, input().split())) for _ in range(N)]

# 섬을 노드로 변환하기 (2부터 시작)
check = 2
for r in range(N):
    for c in range(M):
        if IN[r][c] == 1:
            check = bfs((r, c), check)

# 인접행렬 만들기
G = [[0]*check for _ in range(check)]
make_G(IN)
make_G([list(i) for i in zip(*IN)])

# mst
V = check - 2
E = V - 1
p = list(range(V))
result = kruskal()

print(result)
