# 12865 평범한 배낭

0 - 1 Knapsack

```python
import sys
sys.stdin = open('input.txt')
N, W = map(int, input().split())
bag = [tuple(map(int, input().split())) for _ in range(N)]

knap = [0 for _ in range(W+1)]

for i in range(N):
    for j in range(W, 1, -1):
        if bag[i][0] <= j:
            knap[j] = max(knap[j], knap[j-bag[i][0]] + bag[i][1])

print(knap[-1])
```

이해 X 248ms



## 가장 빠른 풀이

```python
import sys
input = sys.stdin.readline

n,k = map(int, input().split())
ary = [list(map(int, input().split())) for _ in range(n)]

dp = [0]*(k+1)
ary.sort()
for weight, val in ary:
    for j in range(k, weight-1,-1):
        dp[j] = max(dp[j], dp[j-weight] + val)

print(dp[k])
```

140ms