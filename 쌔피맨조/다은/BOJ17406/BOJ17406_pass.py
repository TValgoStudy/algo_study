# https://www.acmicpc.net/problem/17406

import sys
from pandas import DataFrame
from itertools import permutations
sys.stdin = open('input.txt')

from itertools import permutations

drc = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 우 하 좌 상
def my_func(matrix, cal):
    r, c, s = cal
    LU_r, LU_c = r-s, c-s
    RD_r, RD_c = r+s, c+s
    # 회전시켜서 새로운 값을 써 줄 부분 다 -1로 갱신
    for r in range(LU_r, RD_r+1):
        for c in range(LU_c, RD_c+1):
            matrix[r][c] = -1

    # 시작 지점 tmp 리스트 (왼쪽 위에서 오른쪽 아래로 한칸씩)
    tmp = []
    for i in range(s, -1, -1):
        tmp.append((LU_r + i, LU_c + i))

    # 시계 방향으로 회전하는 부분
    while tmp:
        r, c = tmp.pop()
        for dr, dc in drc:
            nr = r + dr
            nc = c + dc
            # 범위 내이고 새로운 값을 써 줄 부분(-1) 이면 갱신
            while LU_r <= nr <= RD_r and LU_c <= nc <= RD_c and matrix[nr][nc] == -1:
                matrix[nr][nc] = IN[r][c]
                # 현재 nr, nc값을 r, c로 하고, 새로운 nr, nc값을 계산
                r, c = nr, nc
                nr, nc = r + dr, c + dc
    # 정 중앙 부분
    matrix[r][c] = IN[r][c]

    return matrix


# 깊은 복사
def my_copy(matrix):
    tmp = []
    for i in matrix:
        tmp.append(i[:])
    return tmp


# 메인 함수
N, M, K = map(int, input().split())
original_IN = [[999]*(M+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
rcs_IN = [list(map(int, input().split())) for _ in range(K)]

# 이 값 괜히 제한 맞춰서 주려고 하지 말고 넉넉하게 주기
arr_A = 999999999
for rotations in permutations(rcs_IN, K):
    # 배열 IN을 회전시키기
    IN = my_copy(original_IN)
    for rot in rotations:
        IN = my_func(my_copy(IN), rot)

    # 배열 IN 에서 행의 최솟값 arr_A 찾기
    for i in range(N+1):
        tmp = sum(IN[i])
        if arr_A > tmp:
            arr_A = tmp
print(arr_A)

# 문제 읽기 15m 문제 풀이 60m => 전체 75m
# 저번 A형 때도 그랬지만 시계방향으로 움직이는 걸 잘 작성 못하는 듯 (연습 필요)