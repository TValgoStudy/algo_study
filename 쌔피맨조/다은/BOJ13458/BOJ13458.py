import sys
sys.stdin = open("input2.txt", "r")
from pandas import DataFrame

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

result = 0
for i in range(N):
    tmp = A[i] - B
    result += 1
    if tmp > 0:
        # a, b = tmp // C, tmp % C
        a, b = divmod(tmp, C)
        result += a + 1 if b else a

print(result)

