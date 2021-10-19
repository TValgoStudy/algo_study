import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def Square(n, A):
    return [
        [sum([A[i][k] * A[k][j] for k in range(n)]) % 1000 for j in range(n)] for i in range(n)
    ]


def mul(n, A, B):
    return [
        [sum([A[i][k] * B[k][j] for k in range(n)]) % 1000 for j in range(n)] for i in range(n)
    ]


def BOJ_10830():
    n, b = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(n)]
    result = [[1 if j == i else 0 for j in range(n)] for i in range(n)]

    while b > 0:
        if b % 2 == 1:  # 홀수이면
            result = mul(n, A, result)  # result = A * result
        A = Square(n, A)  # A = A^2
        b //= 2

    for row in result:
        print(*row)


BOJ_10830()