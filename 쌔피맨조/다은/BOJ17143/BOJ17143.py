import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame
from itertools import product


# 위, 오른쪽, 아래, 왼쪽
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def shark_move(matrix):
    # 상어 이동한 후 내용은 next_matrix에 작성한다
    next_matrix = [[0] * (C+1) for _ in range(R+1)]

    # 원래 matrix에서 상어 이동시키기
    for r, c in product(range(1, R+1), range(1, C+1)):
        # 상어가 없으면 패스
        if not matrix[r][c]:
            continue

        # 상어가 있으면 : s, d, z = 속력, 방향, 크기
        s, d, z = matrix[r][c]

        dist = abs((dr[d] + dc[d]) * s)
        dist2 = dist % (2*R - 2) if dr[d] else dist % (2*C - 2)

        while dist2:
            nr = r + dr[d]
            nc = c + dc[d]
            if 1 <= nr < R+1 and 1 <= nc < C+1:
                r, c = nr, nc
                dist2 -= 1
            else:
                d = (d + 2) % 4

        # 이동 후 내용을 next_matrix에 작성한다.
        if next_matrix[r][c]:
            if next_matrix[r][c][2] < z:
                next_matrix[r][c] = [s, d, z]
        else:
            next_matrix[r][c] = [s, d, z]

    return next_matrix


R, C, M = map(int, input().split())
matrix = [[0]*(C+1) for _ in range(R+1)]

# 상어 정보 인풋
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    if d == 2:
        d = 3
    elif d == 3:
        d = 2
    matrix[r][c] = [s, d-1, z]

# 1. 낚시왕은 오른쪽으로 한 칸씩 이동한다.
result = 0
for c in range(1, C+1):
    # 2. 해당 열에서 땅과 제일 가까운 상어를 잡는다.
    for r in range(1, R+1):
        if matrix[r][c]:
            result += matrix[r][c][2]
            matrix[r][c] = 0
            break
    # 3. 상어가 이동한다.
    matrix = shark_move(matrix)

print(result)
