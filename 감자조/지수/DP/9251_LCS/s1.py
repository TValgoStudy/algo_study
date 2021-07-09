import sys
sys.stdin = open('input.txt')

A = input()
B = input()

N = len(A)
M = len(B)

DP = [[0] * (M+1) for _ in range(N+1)] # 2차원배열

for a in range(1, N+1):
    for b in range(1, M+1):
        if A[a-1] == B[b-1]: # 두개가 같으면 좌상단 + 1
            DP[a][b] = DP[a-1][b-1] + 1
        else: # 다르면 좌, 상 중에 큰것
            DP[a][b] = max(DP[a][b - 1], DP[a-1][b])

print(DP[-1][-1])