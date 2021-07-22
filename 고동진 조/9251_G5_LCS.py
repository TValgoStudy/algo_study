
DP = [[0 for _ in range(len(A) + 1)] for _ in range(len(B) + 1)]
for i in range(1, len(B) + 1):
    for j in range(1, len(A) + 1):
        if A[j - 1] == B[i - 1]:
            DP[i][j] = max(DP[i - 1][j - 1] + 1,  DP[i][j - 1], DP[i - 1][j - 1])
        else:
            DP[i][j] = max(DP[i][j - 1], DP[i - 1][j])

print(max(sum(DP, [])))



A = input()
B = input()
dp = [0] * max(len(A), len(B))
for i in range(len(A)):
    local_max = 0
    for j in range(len(B)):
        if local_max < dp[j]:
            local_max = dp[j]
        elif A[i] == B[j]:
            dp[j] = local_max + 1

print(max(dp))

'''
    max_DP = 3
  A C A Y K P
C 0 1 0 0 0 0
A 1 0 2 0 0 0
P 0 0 0 0 0 3
C 1 2 0 0 0 0
A 1 0 3 0 0 0
K 0 0     4 
  1 2 3 0 4 0
'''







