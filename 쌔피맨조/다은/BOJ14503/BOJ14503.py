import sys
sys.stdin = open("input6.txt", "r")
from pandas import DataFrame

N, M = map(int, input().split())
r, c, d = map(int, input().split())
IN = [list(map(int, input().split())) for _ in range(N)]

# 북 동 남 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

IN[r][c] = 2
stack = 0
while 1:
    # 왼쪽 방향 탐색
    nd = (d - 1) % 4
    nr = r + dr[nd]
    nc = c + dc[nd]

    # if 0 <= nr < N and 0 <= nc < M:
    # 벽이 있어서 nr, nc 확인 안해도 됨

    # 청소할 공간이 있으면 전진하고 청소
    if not IN[nr][nc]:
        IN[nr][nc] = 2
        r, c, d = nr, nc, nd
        stack = 0

    # 청소할 공간이 없으면 회전
    else:
        stack += 1
        d = nd

        # 네 방향 모두 청소가 됐거나 벽이면
        if stack == 4:
            # 한 칸 후진
            back = (d - 2) % 4
            nr = r + dr[back]
            nc = c + dc[back]
            # 만약 벽이면 끝내기
            if IN[nr][nc] == 1:
                break
            # 벽이 아니면 뒤로 돌아가서 반복
            else:
                r, c = nr, nc
                stack = 0


clean = 0
for r in range(N):
    for c in range(M):
        if IN[r][c] == 2:
            clean += 1
print(clean)