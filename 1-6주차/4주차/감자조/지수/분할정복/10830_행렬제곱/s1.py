import sys
from copy import deepcopy
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, B = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
C = [[0] * N for _ in range(N)]
A_copy = deepcopy(A)


for _ in range(B-1):
    for i, row in enumerate(A_copy):
        for j, col in enumerate(zip(*A)):
            C[i][j] = sum([r*c for r, c in zip(row, col)])%1000
    A_copy = deepcopy(C)


for A_row in A_copy:
    print(*A_row)