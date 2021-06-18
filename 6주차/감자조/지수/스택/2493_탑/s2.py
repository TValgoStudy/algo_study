import sys
sys.stdin = open('input.txt')

# DP! 528ms

N = int(input())
tops = list(map(int, input().split()))
tops = [0] + tops

dp = [0] * (N+1) # dp[i] : i번째 탑보다 왼쪽에 있는것 중에 가장 가까운 큰 탑 번호


for j in range(1, N+1):
    if tops[j] < tops[j-1]:
        dp[j] = j-1
    else:
        pre_top = dp[j-1]
        while tops[j] > tops[pre_top] and pre_top:
            pre_top = dp[pre_top]
        dp[j] = pre_top

print(*dp[1:])