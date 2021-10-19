import sys
sys.stdin = open("input.txt", "r")

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0]*3 for _ in range(N)] for _ in range(N)]
answer = 0
direction_dict = {
        # 가로
        0: [(1, 1, 2), (0, 1, 0)],
        # 세로
        1: [(1, 1, 2), (1, 0, 1)],
        # 대각선
        2: [(1, 1, 2), (1, 0, 1), (0, 1, 0)]
    }
dp[0][1][0] = 1

for i in range(N):
    for j in range(N):
        if not arr[i-1][j-1] and not arr[i-1][j-2]:
            dp[i][j][0] += 1
        if not arr[i][j-1] and not arr[i][j-2]:
            dp[i][j][0] += 1
        if not arr[i-1][j] and not arr[i-2][j]:
            dp[i][j]

print(answer)