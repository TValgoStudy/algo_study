# python 68ms

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

L, C = map(int, input().split())
code = sorted(list(input().split()))

# code로 만들 수 있는 L자리 암호를 모두 출력
# 암호는 최소 한개의 모음, 최소 두개의 자음으로 구성되어 있으며, 정렬되어 있다.

# 완전탐색 방법 : 길이가 L인 순열을 구한다(알파벳을 선택 한다 or 안한다). 최소 조건을 만족하고, 정렬되게끔 만든다.
# 백트래킹? 더 이상 암호를 완성할 수 없다고 판단되는 경우 -> 암호의 길이보다, 후보의 길이가 적은 경우?

jamoCnt = [[0, 0] for _ in range(C)]

def init():
    for j in range(C-1, -1, -1):
        if code[j] in ('a', 'e', 'i', 'o', 'u'):
            if j == C - 1:
                jamoCnt[j] = [0, 1]
            else:
                jamoCnt[j] = [jamoCnt[j+1][0], jamoCnt[j+1][1] + 1]
        else:
            if j == C - 1:
                jamoCnt[j] = [1, 0]
            else:
                jamoCnt[j] = [jamoCnt[j+1][0] + 1, jamoCnt[j+1][1]]


def setPassWord(n, idx, password, jaCnt, moCnt):

    # 백트래킹1
    if L - n > C - idx: # 선택해야하는 것보다 선택지가 적게 남는 경우
        return

    if n == L:
        if jaCnt >= 2 and moCnt >= 1:
            print(password)
        return

    # 백트래킹2
    if jaCnt + jamoCnt[idx][0] < 2 or  moCnt + jamoCnt[idx][1] < 1:
        return

    for i in range(idx, C):
        if code[i] in ('a', 'e', 'i', 'o', 'u'):
            setPassWord(n+1, i+1, password+code[i], jaCnt, moCnt + 1)
        else:
            setPassWord(n + 1, i + 1, password + code[i], jaCnt + 1, moCnt)

init()
setPassWord(0, 0, '', 0, 0)