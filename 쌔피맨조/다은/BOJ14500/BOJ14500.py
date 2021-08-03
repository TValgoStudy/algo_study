import sys
sys.stdin = open("input4.txt", "r")
from pandas import DataFrame

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def func(q, my_sum):
    global result

    # 4개 선택하면 그만
    n = len(q)
    if n == 4:
        if result < my_sum:
            result = my_sum
        return

    # q와 인접한 영역 중 최대값 찾기
    # target r, target c, val(최대값)
    tr, tc, val = 0, 0, 0
    # q : 현재까지 선택한 테트로미노 좌표들
    for i in range(n):
        r, c = q[i]
        # q에서 하나씩 꺼내면서 상하좌우 탐색
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            # 맵 안이고 아직 방문하지 않았으면 (q에 등록하지 않은 값이면)
            if (0 <= nr < N and 0 <= nc < M) and not visited[nr][nc]:
                # 기존 val보다 더 최대값을 찾았으면 갱신
                if val < IN[nr][nc]:
                    val = IN[nr][nc]
                    tr, tc = nr, nc

    # 찾은 최대값을 q에 등록하여 재귀
    visited[tr][tc] = 1
    func(q + [(tr, tc)], my_sum + IN[tr][tc])
    visited[tr][tc] = 0


N, M = map(int, input().split())
IN = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
n, result = 0, 0

# 모든 위치에서 탐색 시작
for r in range(N):
    for c in range(M):
        visited[r][c] = 1
        func([(r, c)], IN[r][c])
        visited[r][c] = 0

print(result)