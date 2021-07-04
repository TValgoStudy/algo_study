import sys
sys.stdin = open('input.txt')

def pre_processing(P, m):
    j = 0 # 접미사 인덱스
    k = -1 # 접미사 일치 인덱스
    pi = [0] * (m+1)
    pi[j] = k # 0번 인덱스는 -1로
    while j < m:
        if k == -1 or P[j] == P[k]:
            j += 1
            k += 1
            pi[j] = k
        else:
            k = pi[k]
    return pi


def kmp(A, P, n, m):
    i = j = 0
    pi = pre_processing(P, m)
    while i < n:
        if j == -1 or A[i] == P[j]:
            i += 1
            j += 1
        else:
            j = pi[j]
        if j == m:  # Success
            res.append(i-m+1)
            j = pi[j]

A = input()
P = input()
res = []
kmp(A, P, len(A), len(P))
print(len(res))
print(' '.join(map(str, res)))