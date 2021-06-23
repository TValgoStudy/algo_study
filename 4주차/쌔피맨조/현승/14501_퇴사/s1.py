# dp
import sys
sys.stdin = open("input.txt", "r")
import time
start = time.time()

N = int(input())
T = [0 for _ in range(N+1)]
P = [0 for _ in range(N+1)]
dp = [0 for _ in range(N+2)]
for i in range(1, N+1):
    T[i], P[i] = map(int, input().split())

for i in range(1, N+1):
    # 이전 최대값과 현재 최대값중 큰 것을 선택
    dp[i] = max(dp[i-1], dp[i])

    # end_day 상담이 종료되는 날
    end_day = i + T[i]

    # 종료날이 N+1 일 이하일 경우 갱신 가능하다
    if end_day <= N+1:
        # 상담비의 최대값 = (상담시작날 최대값 + 상담비용)과 기존의 상담비용 중 큰 것
        dp[end_day] = max(dp[i] + P[i], dp[end_day])

print(max(dp[N+1], dp[N]))

print("time: ", time.time() - start)
