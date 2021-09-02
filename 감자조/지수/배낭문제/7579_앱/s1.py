import sys
sys.stdin = open('input.txt')

q = lambda : map(int, sys.stdin.readline().split())

N, M = q()  # M : 필요한 메모리 = 베낭 용량
m = list(q())  # 메모리 = 무게
c = list(q())  # 활성화하는데 드는 비용 = 가치

dp = [[0 for _ in range(M+1)] for __ in range(N+1)]

for i in range(1, N+1):
    memory, value = m[i-1], c[i-1]
    for j in range(memory, M+1):
        dp[i][j] = max(value + dp[i-1][j-memory], dp[i-1][j])


print(dp[-1])