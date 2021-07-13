N = int(input())
arr = []

for i in range(N):
    arr.append(list(map(int,input().split())))

dp=[0 for i in range(len(arr)+1)]
for i in range(len(arr)+1):
    for j in range(i):
        if j + arr[j][0] <= i:
            dp[i] = max(dp[j] + arr[j][1], dp[i])

print(dp[-1])