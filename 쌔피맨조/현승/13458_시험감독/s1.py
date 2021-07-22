import sys
sys.stdin = open("input.txt", "r")
# input = sys.stdin.readline
# 부감독관이 더 많이 감시할 수 있는 경우

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

ans = 0

for i in range(N):
    # total = C*mok + remain
    total = A[i] - B
    if total > 0:
        mok = total // C
        remain = total % C
        if remain:
            ans += mok + 1
        else:
            ans += mok


print(ans + N)