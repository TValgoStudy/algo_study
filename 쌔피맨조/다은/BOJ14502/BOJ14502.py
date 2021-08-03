import sys
sys.stdin = open("input5.txt", "r")
from pandas import DataFrame


### 실패

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(s, IN):
    q = [s]
    IN[s[0]][s[1]] = 2
    while q:
        r, c = q.pop(0)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if (0 <= nr < N and 0 <= nc < M) and not IN[nr][nc]:
                q.append((nr, nc))
                IN[nr][nc] = 2


def my_func(num, IN, a, b):
    global result

    # 벽 3개를 세웠을 때
    if num == 3:
        # 바이러스 확장
        for vr, vc in virus:
            bfs((vr, vc), IN)
        # 안전영역 계산
        safe = 0
        for n in range(N):
            for m in range(M):
                if IN[n][m] == 0:
                    safe += 1
        # result 갱신
        if result < safe:
            result = safe
        return

    # 벽 3개를 아직 안 세웠을 때
    for r in range(a, N):
        for c in range(b, M):
            # 일반 땅일 때
            if IN[r][c] == 0:
                # 벽을 세우고 다음 단계로
                IN[r][c] = 1
                IN_copy = [i[:] for i in IN]
                my_func(num+1, IN_copy, r, c)
                IN[r][c] = 0
            # 벽을 세우지 않고 다음 단계로
            my_func(num, IN, r, c)


N, M = map(int, input().split())
IN = [list(map(int, input().split())) for _ in range(N)]

virus = []
for r in range(N):
    for c in range(M):
        if IN[r][c] == 2:
            virus.append((r, c))

result = 0
my_func(0, IN, 0, 0)
print(result)




###### 성공
#
# from itertools import permutations
#
# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]
#
# def bfs(s, IN):
#     q = [s]
#     IN[s[0]][s[1]] = 2
#     while q:
#         r, c = q.pop(0)
#         for i in range(4):
#             nr = r + dr[i]
#             nc = c + dc[i]
#             if (0 <= nr < N and 0 <= nc < M) and not IN[nr][nc]:
#                 q.append((nr, nc))
#                 IN[nr][nc] = 2
#
# N, M = map(int, input().split())
# IN = [list(map(int, input().split())) for _ in range(N)]
#
# node = []
# virus = []
# for r in range(N):
#     for c in range(M):
#         if IN[r][c] == 0:
#             node.append((r, c))
#         if IN[r][c] == 2:
#             virus.append((r, c))
#
# result = 0
# for i in permutations(node, 3):
#     IN_copy = [i[:] for i in IN]
#
#     # 벽 만들기
#     for r, c in i:
#         IN_copy[r][c] = 1
#
#     # 바이러스 확장
#     for vr, vc in virus:
#         bfs((vr, vc), IN_copy)
#
#     # 안전영역 계산
#     safe = 0
#     for n in range(N):
#         for m in range(M):
#             if IN_copy[n][m] == 0:
#                 safe += 1
#
#     # result 갱신
#     if result < safe:
#         result = safe
#
# print(result)