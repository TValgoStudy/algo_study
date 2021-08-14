import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def solution():
    n, k = map(int, input().split())
    arr = input()
    stack = []

    for a in arr:
        while stack and stack[-1] < a and k > 0:
            stack.pop()
            k -= 1
        stack.append(a)

    return ''.join(stack)

print(solution())