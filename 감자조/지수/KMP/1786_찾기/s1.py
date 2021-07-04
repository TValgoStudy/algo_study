import sys
sys.stdin = open('input.txt')

T = input()
P = input()

def findNext(P):
    len_P = len(P)
    moveIdx = [0] * len_P # 불일치 발생 시 이동할 인덱스 정보

    for i in range(1, len_P):
        for j in range(i-1): # 일치하는 부분의 길이
            if P[:j+1] == P[i-1-j:i]: # 0~j와 i-j-1~i-1이 같은지
                moveIdx[i] = j + 1 # 같다면 그 다음 인덱스를 저장(j까지 같으니까 j까지 안봐도 됨)

    return moveIdx


def KMP(T, P):
    moveIdx = findNext(P)

    lenT, lenP = len(T), len(P)
    t = 0 # target index
    p = 0 # pattern index
    cnt = 0
    result = []

    while t < lenT:
        while t < lenT and p < lenP:
            if T[t] != P[p]: # 불일치 발생
                if moveIdx[p] == 0:
                    t -= p
                else:
                    t -= 1
                p = moveIdx[p] - 1
            t += 1
            p += 1

        if p == lenP:
            result.append(t-lenP+1)
            cnt += 1
            p = 0

    print(cnt)
    print(*result)

KMP(T, P)