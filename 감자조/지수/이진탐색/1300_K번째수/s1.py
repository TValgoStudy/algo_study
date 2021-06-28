import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, k = int(input()), int(input())
l, r = 1, k #point①

while l <= r:
    m = (l + r) //  2

    cnt = 0
    for i in range(1, N+1):
        cnt += min(N, m//i)

    if cnt >= k :
        result = m
        r = m - 1
    else:
        l = m + 1

print(result)