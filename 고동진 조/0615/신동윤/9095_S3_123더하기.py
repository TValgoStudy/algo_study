T = int(input())
for tc in range(1, T+1):
    N = int(input())
    DP = [0] * (N + 4)
    DP[0] = 1
    for i in range(0, N + 1):
        DP[i + 1] += DP[i]
        DP[i + 2] += DP[i]
        DP[i + 3] += DP[i]

    print(DP[N])