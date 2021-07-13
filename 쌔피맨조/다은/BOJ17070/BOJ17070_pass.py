import sys
from pandas import DataFrame
sys.stdin = open('input.txt')

N = int(input())
IN = [list(map(int, input().split())) for _ in range(N)]

# input IN[r][c] = [가로 방법 수, 세로 방법 수, 대각선 방법 수]
for r in range(N):
    for c in range(N):
        if IN[r][c] == 1:
            IN[r][c] = -1
        else:
            IN[r][c] = [0, 0, 0]
IN[0][1] = [1, 0, 0]

# [r][c]에서 [nr][nc]로, "가로 방법"으로 갈 수 있는 방법 수 체크
def row_check(r, c, k):
    nr = r + 0
    nc = c + 1
    # map 범위 내이면서 [nr][nc]가 벽(-1)이 아닐 때
    if 0 <= nr < N and 0 <= nc < N and IN[nr][nc] != -1:
        IN[nr][nc][0] += IN[r][c][k]

# [r][c]에서 [nr][nc]로, "세로 방법"으로 갈 수 있는 방법 수 체크
def col_check(r, c, k):
    nr = r + 1
    nc = c + 0
    # map 범위 내이면서 [nr][nc]가 벽(-1)이 아닐 때
    if 0 <= nr < N and 0 <= nc < N and IN[nr][nc] != -1:
        IN[nr][nc][1] += IN[r][c][k]

# [r][c]에서 [nr][nc]로, "대각선 방법"으로 갈 수 있는 방법 수 체크
def dia_check(r, c, k):
    nr = r + 1
    nc = c + 1
    # map 범위 내이면서 [nr][nc]가 벽(-1)이 아닐 때
    if 0 <= nr < N and 0 <= nc < N and (IN[nr][nc] != -1 and IN[nr - 1][nc] != -1 and IN[nr][nc - 1] != -1):
        IN[nr][nc][2] += IN[r][c][k]

# main 함수
for r in range(N):
    for c in range(N):
        # 벽이면 할 필요 X
        if IN[r][c] == -1:
            continue

        # 가로 : 가로&대각선으로 갈 수 있으니 둘만 체크
        if IN[r][c][0]:
            row_check(r, c, 0)
            dia_check(r, c, 0)

        # 세로 : 세로&대각선으로 갈 수 있으니 둘만 체크
        if IN[r][c][1]:
            col_check(r, c, 1)
            dia_check(r, c, 1)

        # 대각선 : 가로&세로&대각선으로 갈 수 있으니 셋 체크
        if IN[r][c][2]:
            row_check(r, c, 2)
            col_check(r, c, 2)
            dia_check(r, c, 2)

# print(DataFrame(IN))
# sum(-1) 고려 안해줘서 런타임 에러났음 이거 typeError 난다.
# 여기서 2페일 이후 통과 (읽기 15m => 문풀 50m => 수정 70m)
if IN[N-1][N-1] != -1:
    print(sum(IN[N-1][N-1]))
else:
    print(0)
