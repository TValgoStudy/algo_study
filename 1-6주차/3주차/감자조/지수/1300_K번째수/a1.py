import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def parametric_search_max(f, left, right):
    ans = 0
    while left < right:
        middle = (left + right) // 2
        if f(middle):
            ans = max(ans, middle)
            left = middle + 1
        else:
            right = middle

    if f(left):
        ans = max(ans, left)

    return ans


def check(N, K, n):
    count = 0
    for i in range(1, N + 1):
        count += min((n - 1) // i, N)
    if count < K:
        return True
    else:
        return False


N = int(input())
K = int(input())
print(parametric_search_max(lambda x: check(N, K, x), 1, min(int(1e9), N*N)))