# DP 틀림
# 최단 거리가 아니라 최단 박살이라서 이렇게 푸는게 아닌듯

import sys
sys.stdin = open('input.txt')

C, R = map(int, input().split())
arr = [list(map(int, list(input()))) for _ in range(R)]

def solution():
    for r in range(R):
        for c in range(C):
            if r == 0 and c == 0: continue
            elif r == 0:
                arr[r][c] = arr[r][c] + arr[r][c-1]
            elif c == 0:
                arr[r][c] = arr[r][c] + arr[r-1][c]
            else:
                arr[r][c] += min(arr[r][c-1], arr[r-1][c])

    return arr[R-1][C-1]

print(solution())