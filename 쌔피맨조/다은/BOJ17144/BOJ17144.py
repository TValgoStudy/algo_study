import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame

from itertools import product


def diffusion():
    next_IN = [[0]*C for _ in range(R)]
    for r, c in product(range(R), range(C)):
        # 공청기면 패스
        if IN[r][c] == -1:
            continue

        cell_cnt = 0
        for dr, dc in drc:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C and IN[nr][nc] != -1:
                # 주위로부터 r, c로 확산되는 미세먼지의 양
                next_IN[r][c] += IN[nr][nc] // 5
                # 확산되거나, 확산되는 cell 의 개수
                cell_cnt += 1
        # r, c에서 주위로 확산되는 미세먼지의 양
        next_IN[r][c] += IN[r][c] - (IN[r][c] // 5) * cell_cnt

    next_IN[top[0]][top[1]] = -1
    next_IN[bottom[0]][bottom[1]] = -1
    return next_IN


def move(top_or_bottom: tuple, cc_or_ccw: list):
    r, c = top_or_bottom
    tmp, start = 0, 0
    # 한 바퀴 돌기
    for dr, dc in cc_or_ccw:
        while 1:
            nr, nc = r + dr, c + dc
            # 시작도 안했으면 먼저 시작하고, 시작한 이후엔 nr, nc가 공청기 = -1 이면 중지
            if 0 <= nr < R and 0 <= nc < C and (not start or IN[nr][nc] != -1):
                IN[nr][nc], tmp = tmp, IN[nr][nc]
                r, c = nr, nc
                start = 1
            else:
                break


R, C, T = map(int, input().split())
IN = [list(map(int, input().split())) for _ in range(R)]
drc = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 공청기 일 때, top이 비었으면 먼저 넣어주기
top, bottom = 0, 0
for r, c in product(range(R), range(C)):
    if IN[r][c] == -1:
        if not top:
            top = (r, c)
        else:
            bottom = (r, c)

# 공청기는 1열에 붙어있으므로 항상 오른쪽으로 출발
# top은 cc 방향으로 , bottom은 ccw 방향으로
cc = [(0, 1), (-1, 0), (0, -1), (1, 0)]
ccw = [(0, 1), (1, 0), (0, -1), (-1, 0)]

while T:
    IN = diffusion()
    move(top, cc)
    move(bottom, ccw)
    T -= 1

result = 0
for l in IN:
    result += sum(l)
print(result + 2)

