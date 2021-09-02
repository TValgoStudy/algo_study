import sys
sys.stdin = open('input.txt')

# 464ms (python)
# https://life-with-coding.tistory.com/316 여기 참고!

q = lambda : map(int, sys.stdin.readline().split())

N, M = q()  # M : 필요한 메모리 = 베낭 용량
m = list(q())  # 메모리 = 무게
c = list(q())  # 활성화하는데 드는 비용 = 가치
max_cost = sum(c)
cnt = 0

dp = [0 for _ in range(max_cost+1)] # 0 ~ 모든 코스트 합

# dp 배열 만드는 부분
for i in range(0, N): # 앱 순회
    memory, cost = m[i], c[i]

    # 뒤부터 하는 이유, 앞부터 하면 dp[j - cost]이거 때문 누적됨
    for j in range(max_cost, cost-1, -1):
        dp[j] = max(dp[j - cost] + memory, dp[j])

# 정답 내는 부분
for i in range(max_cost + 1):
    if dp[i] >= M:
        print(i)
        break