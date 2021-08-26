import sys
from pandas import DataFrame
sys.stdin = open("input.txt", "r")

# S: 톱니바퀴 입력
S, T = [input() for i in range(4)], [0]*4


def mv(n, l):
    return (n+8+l) % 8


def r(k, c, p):
    n = k + p
    # n이 범위 내이고, 맞닿은 톱니바퀴가 서로 다르면 연쇄로 재귀
    if n != -1 and n != 4 and S[k][mv(T[k], 2*p)] != S[n][mv(T[n], -2*p)]:
        r(n, -c, p)
    T[k] = mv(T[k], -c)


# a: 몇 번째 톱니바퀴, b: 어느 방향 회전
for _ in range(int(input())):
    a, b = map(int, input().split())
    a -= 1
    # 톱니바퀴를 b 방향으로 회전 + 오른쪽으로 이동
    r(a, b, 1)
    T[a] = mv(T[a], b)
    # 톱니바퀴를 b 방향으로 회전 + 왼쪽으로 이동
    r(a, b, -1)


print(sum([2**i*(int(S[i][T[i]])) for i in range(4)]))