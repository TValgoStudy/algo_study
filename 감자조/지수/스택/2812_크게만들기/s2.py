import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def solution():
    n, k = map(int, input().split())
    arr = input()
    stack = []
    rmv = k
    l = 0

    for a in arr:
        while stack and stack[-1] < a and rmv > 0:
            stack.pop()
            rmv -= 1
            l -= 1
        stack.append(a)
        l += 1

        if l > n - k:
            break

    return ''.join(stack[:n-k])

print(solution())