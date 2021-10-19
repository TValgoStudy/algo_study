# dp
import sys
# input = sys.stdin.readline
sys.stdin = open("input.txt", "r")
import time
start = time.time()

def dp(day):
    if day >= N+1:
        return 0

    if memo[day]:
        return memo[day]

    end_day = day + T[day]
    if end_day <= N+1:
        memo[day] = max(dp(day+1), dp(end_day) + P[day])
    else:
        memo[day] = memo[day+1]
    return memo[day]


N = int(input())
T = [0 for _ in range(N+1)]
P = [0 for _ in range(N+1)]
memo = [0 for _ in range(N+2)]
for i in range(1, N+1):
    T[i], P[i] = map(int, input().split())

ans = dp(1)

print(ans)

print("time: ", time.time() - start)
