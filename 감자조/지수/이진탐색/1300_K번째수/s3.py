import sys
sys.stdin = open('eval_input.txt')
input = sys.stdin.readline

N, k = int(input()), int(input())
l, r = 1, k #point①
result = 0

def getCnt(m):
    cnt = 0
    for i in range(1, N + 1):
        cnt += min(N, m // i) #point②

    return cnt

def binarySearch(l, r):
    while l <= r:
        m = (l + r) //  2

        if getCnt(m) >= k :
            r = m-1
        else:
            l = m+1
    return l #point③

print(binarySearch(l, r))