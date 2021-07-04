import sys
sys.stdin = open('input.txt')

# 796

def getpartialmatch(P):
    m = len(P)
    pi = [0 for _ in range(m)] # 불일치 발생시 돌아갈 곳

    begin = 1
    matched = 0
    while begin + matched < m:
        if P[begin + matched] == P[matched]:
            matched += 1
            pi[begin + matched - 1] = matched

        else:
            if matched == 0:
                begin += 1
            else:
                begin += matched - pi[matched - 1]
                matched = pi[matched - 1]
    return pi


def KMP(T, P):
    n = len(T)
    m = len(P)
    result = []
    pi = getpartialmatch(P)

    begin = 0
    matched = 0
    while begin <= n - m:
        if matched < m and T[begin + matched] == P[matched]: # 일치
            matched += 1
            if matched == m: # 끝까지 다 매칭이면 결과에 추가
                result.append(begin+1)
        else: # 불일치
            if matched == 0: # 매칭된게 없으면
                begin += 1 # 한칸만 이동해서 시작
            else: # 매칭된게 있으면
                begin += matched - pi[matched - 1] # 일치했던 길이 - 돌아간 곳
                matched = pi[matched - 1] # 이미 매치되서 안봐도 되는 길이
    return result


T = str(input())
P = str(input())

x = KMP(T, P)

print(len(x))
print(*x)
