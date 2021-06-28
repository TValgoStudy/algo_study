import sys
sys.stdin = open('input.txt')

# 그냥 반복문 시간
# 시간복잡도: O(nlogn) n^2?
# 시간초과

N = int(input())
tops = list(map(int, input().split()))

ans = [0] * N

for i in range(N-1, -1, -1):
    cur = tops[i]
    for j in range(i-1, -1, -1):
        if tops[j] > cur:
            ans[i] = j + 1
            break

print(*ans)

