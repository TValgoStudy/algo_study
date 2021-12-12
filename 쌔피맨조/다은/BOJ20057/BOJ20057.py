import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame


ratio = [[0]*5 for _ in range(5)]
ratio[0][2] = ratio[4][2] = 0.02
ratio[1][1] = ratio[3][1] = 0.1
ratio[1][2] = ratio[3][2] = 0.07
ratio[1][3] = ratio[3][3] = 0.01
ratio[2][0] = 0.05
ratio[2][1] = -1

ratio90 = [list(i) for i in zip(*ratio[::-1])]
ratio180 = [list(i) for i in zip(*ratio90[::-1])]
ratio270 = [list(i) for i in zip(*ratio180[::-1])]

# 좌 하 우 상
dr = [0, 1, 0, -1]
dc = [-1, 0, 1, 0]

def go(pr, pc, d):
    global result

    # 방문체크
    matrix_check[pr][pc] = 1

    # 방향에 따른 토네이도 비율
    if d == 0: ratio_d = ratio
    elif d == 1: ratio_d = ratio270
    elif d == 2: ratio_d = ratio180
    else: ratio_d = ratio90

    # y 좌표
    nr, nc = pr + dr[d], pc + dc[d]
    # y 모래 양
    sand = matrix[nr][nc]

    # y 모래 이동
    move_sand = 0
    for r in range(-2, 3):
        for c in range(-2, 3):
            # 다음 좌표
            nnr, nnc = nr + r, nc + c

            # a 칸으로 이동하는 모래면 따로 연산
            if ratio_d[r+2][c+2] == -1:
                ar, ac, = nnr, nnc
                continue

            # 비율이 써있는 칸이면 연산
            move_sand_ratio = int(sand * ratio_d[r+2][c+2])
            move_sand += move_sand_ratio
            if 0 <= nnr < N and 0 <= nnc < N:
                matrix[nnr][nnc] += move_sand_ratio
            else:
                result += move_sand_ratio
    # a칸 모래 연산
    if 0 <= ar < N and 0 <= ac < N:
        matrix[ar][ac] += sand - move_sand
    else:
        result += sand - move_sand

    # x 모래 이동
    matrix[pr][pc], matrix[nr][nc] = 0, matrix[pr][pc]

    nd = (d + 1) % 4
    if matrix_check[nr+dr[nd]][nc+dc[nd]]:
        nd = d
    return nr, nc, nd


N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
matrix_check = [[0]*N for _ in range(N)]

result = 0
r = c = N // 2
d = 0

while r != 0 or c != 0:
    r, c, d = go(r, c, d)


print(result)


