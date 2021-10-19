import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, k = int(input()), int(input())
l, r = 1, k #point①
result = 0

def getCnt(m):
    cnt = 0
    for i in range(1, N + 1):
        cnt += min(N, m // i)

    return cnt

def binarySearch(l, r):
    global result
    if l > r:
        return

    m = (l + r) //  2

    if getCnt(m) >= k :
        result = m
        binarySearch(l, m-1)
    else:
        binarySearch(m+1, r)


binarySearch(l, r)
print(result)