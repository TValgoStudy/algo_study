import sys
from pandas import DataFrame
sys.stdin = open("input.txt", "r")


def check(matrix):
    for c in range(1, N+1):
        start_c = c
        for r in range(1, H+1):
            if matrix[r][c]:
                c = matrix[r][c]
        if start_c != c:
            return False
    return True


def func(num, matrix, cr, cc, col_state):
    global result

    # 홀수개가 3개 이상이면 가망 X
    cnt = 0
    for n in col_state:
        if n % 2:
            cnt += 1
    # 이거 왜 num + cnt > 3 이 안되지 ?
    if num + cnt > 4:
        return

    if check(matrix):
        if result > num or result == -1:
            result = num
        return

    for r in range(cr, H+1):
        for c in range(1, N):
            if r == cr and c <= cc:
                continue
            # 인접한 두 점이 0이면 가로선 만들기
            if not matrix[r][c] and not matrix[r][c+1] and num < 3:
                matrix_copy = [i[:] for i in matrix]
                matrix_copy[r][c] = c + 1
                matrix_copy[r][c+1] = c
                col_state_copy = col_state[:]
                col_state_copy[c] += 1
                func(num+1, matrix_copy, r, c, col_state_copy)
    return


# 세로선의 개수 column N, 가로선의 개수 M, 세로선마다 가로선을 놓을 수 있는 위치의 개수 row H
N, M, H = map(int, input().split())

matrix = [[0]*(N+1) for _ in range(H+1)]
for _ in range(M):
    a, b = map(int, input().split())
    matrix[a][b] = b+1
    matrix[a][b+1] = b

col_state = [0] * (N+1)
for c in range(1, N):
    for r in range(1, H+1):
        if matrix[r][c] == c+1:
            col_state[c] += 1

result = -1
func(0, matrix, 1, 0, col_state)
print(result)

# -------------------------------------------












"""

col_line = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    col_line[b].append(a)

for _ in range(N+1):
    col_line[_].sort()

result = 0
stack = []
for i in range(N):
    # 비어있으면 통과
    if not col_line[i]:
        continue
        
    # 안비어있으면 스택으로 연산한다
    stack = []
    while col_line[i]:
        # 다음 세로 사다리 비교해서, 다음 세로 사다리가 없으면
        if not col_line[i+1]:
            # 현재 사다리가 홀수개면 가로선 하나 필요
            # 짝수개면 가로선 필요 없음
            if len(col_line[i]) % 2:
                result += 1
            break
            
        # 다음 세로 사다리가 있으면
        # 맨 앞에있는 거 하나 뽑아오고
        point = col_line[i].pop(0)
        
        # point다음이고 point에 가장 가까운, 다음 세로줄에 있는 가로선을 찾는다
        next_col_point = 0
        for p in col_line[i+1]:
            if p > point:
                next_col_point = p
                break
        # 만약 next_col_point가 없으면 pop으로 하나 미리 빼놨으니까
        # 홀수개면 ok고 짝수개면 하나 추가해줘야 한다
        if not next_col_point:
            if not (len(col_line[i]) % 2):
                result += 1
            break
        # next_col_point가 있으면
        
"""