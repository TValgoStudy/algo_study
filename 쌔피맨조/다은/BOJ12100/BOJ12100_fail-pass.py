import sys
sys.stdin = open("input2.txt", "r")
from pandas import DataFrame


# 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def plus(IN):
    for r in range(N):
        tmp = []
        P1, P2 = 0, 1
        while P2 < N:
            if IN[r][P1] == 0:
                if P2 == N-1:
                    tmp.append(IN[r][P2])
                P1, P2 = P2, P2 + 1
            elif IN[r][P2] == 0:
                if P2 == N-1 and IN[r][P1]:
                    tmp.append(IN[r][P1])
                P2 += 1
            elif IN[r][P1] == IN[r][P2]:
                tmp.append(IN[r][P1] * 2)
                if P2 == N - 2:
                    tmp.append(IN[r][P2 + 1])
                P1, P2 = P2 + 1, P2 + 2
            else:
                tmp.append(IN[r][P1])
                if P2 == N - 1:
                    tmp.append(IN[r][P2])
                P1, P2 = P2, P2 + 1
        IN[r] = tmp + [0] * (N - len(tmp))


def func(GO, idx, IN):
    global result

    # if GO == [0, 2, 2, 2 ,2]:
    #     print('sss')
    if idx >= 5:
        for r in range(N):
            for c in range(N):
                if result < IN[r][c]:
                    # print(GO, IN[r][c])
                    result = IN[r][c]
        return

    if GO[-1] == 0:
        IN = [list(i) for i in zip(*IN)][::-1]
        plus(IN)
        IN = [list(i[::-1]) for i in zip(*IN)]
    elif GO[-1] == 1:
        IN = [list(i[::-1]) for i in zip(*IN)]
        plus(IN)
        IN = [list(i) for i in zip(*IN)][::-1]
    elif GO[-1] == 2:
        plus(IN)
    else:
        IN = [list(i) for i in zip(*IN)][::-1]
        IN = [list(i) for i in zip(*IN)][::-1]
        plus(IN)
        IN = [list(i) for i in zip(*IN)][::-1]
        IN = [list(i) for i in zip(*IN)][::-1]

    for i in range(4):
        IN_copy = [i[:] for i in IN]
        func(GO + [i], idx + 1, IN_copy)


N = int(input())
IN = [list(map(int, input().split())) for _ in range(N)]

# IN = [list(i) for i in zip(*IN)][::-1] # 반시계 90
# IN = [list(i[::-1]) for i in zip(*IN)] # 시계 90

result = 0
for r in range(N):
    for c in range(N):
        if IN[r][c] > result:
            result = IN[r][c]

for j in range(4):
    IN_copy = [i[:] for i in IN]
    func([j], 0, IN_copy)

print(result)
