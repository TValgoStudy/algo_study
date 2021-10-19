# dp
import sys
# input = sys.stdin.readline
sys.stdin = open("input.txt", "r")
import time
start = time.time()


N = int(input())
T = [0 for _ in range(N+1)]
P = [0 for _ in range(N+1)]
dp = [0 for _ in range(N+2)]
for i in range(1, N+1):
    T[i], P[i] = map(int, input().split())

for i in range(N, 0, -1):

    end_day = i + T[i]

    if end_day <= N+1:
        dp[i] = max(dp[i+1], dp[end_day] + P[i])
    else:
        dp[i] = dp[i+1]

print(dp[1])
print(dp)
print("time: ", time.time() - start)
