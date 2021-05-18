import sys

input = sys.stdin.readline

from itertools import permutations

N, M, K = list(map(int, input().split()))
A_ori = [list(map(int, input().split())) for _ in range(N)]

R = []
for _ in range(K):
    tmp = list(map(int, input().split()))
    tmp[0] -= 1
    tmp[1] -= 1
    R.append(tmp)


def rotate(R, C, S):
    for s in range(1, S + 1):
        tmp = 0
        r = R - s
        for c in range(C - s, C + s):
            A[r][c], tmp = tmp, A[r][c]

        c = C + s
        for r in range(R - s, R + s):
            A[r][c], tmp = tmp, A[r][c]

        r = R + s
        for c in range(C + s, C - s, -1):
            A[r][c], tmp = tmp, A[r][c]

        c = C - s
        for r in range(R + s, R - s, -1):
            A[r][c], tmp = tmp, A[r][c]

        A[R - s][C - s] = tmp


out = 100 * 50 + 1
for order in permutations(R, len(R)):
    A = [a[:] for a in A_ori]
    for i in range(len(order)):
        rotate(*order[i])
    out = min(out, min(sum(a) for a in A))
print(out)