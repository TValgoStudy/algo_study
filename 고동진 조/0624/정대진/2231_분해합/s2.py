# Wrong //으로 몫을 구하면 잘못된 값이 나옴
N = int(input())
# 117 -> 99, 216 -> 198
weight = [10**i+1 for i in range(7)]
digit = [9 for _ in range(7)]
total = 0
idx = 0
while total < N:
    total += weight[idx]*digit[idx]
    idx += 1
idx -= 1
if total == N:
    for i in range(idx,-1,-1):
        print(digit[i], end='')
else:
    for i in range(idx, -1, -1):
        digit[i] = N//weight[i]
        N -= digit[i]*weight[i]
    if N == 0:
        for i in range(idx,-1,-1):
            print(digit[i], end='')
    else:
        print(0)