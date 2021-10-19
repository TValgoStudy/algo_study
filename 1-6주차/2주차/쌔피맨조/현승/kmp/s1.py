import sys
sys.stdin = open("input.txt", "r")
import time
start = time.time()

'''
kmp 알고리즘
- 문자를 비교해 나가다가 값이 다르면 최장접두사의 다음 인덱스로 돌아가 다시 비교해나가는 알고리즘
- 원리도 어렵고 구현도 아이디어가 필요함
- 비교한 곳까지의 접두사와 접미사가 같은 구간이 없으면 비교한 곳 이전은 같은 문자 시작점이 존재할 리 없다.
'''


# pi 함수 구현
'''
- pi[i] = 최장 접두사의 길이 : 0~i까지의 부분 문자열에서 접두사 = 접미사인 길이 중 최대값
- point : 최장 접두사의 길이는 결국 최장접두사 다음 인덱스를 가리킨다. 
i : 현재 인덱스(접미사의 끝글자 인덱스)
j : 최장 접두사의 길이
1-1. p[i]와 p[j]가 같다면? j + 1을 pi[i]에 저장, 
1-2. p[i]와 p[j]가 다르다면? 같아질 때까지 j = pi[j-1](바로이전까지의 최대접두사 다음의 인덱스)
'''
def get_pi(p: str):
    # i : 접미사의 끝글자 인덱스, j : 최장접두사의 길이
    i, j = 1, 0
    pi = [0 for _ in range(len(p))]
    while i < len(p):

        # 현재 인덱스와 최장접두사 다음 인덱스 값이 같은 경우
        if pi[i] == pi[j]:
            # 최장접두사길이 + 1
            j += 1
            pi[i] = j
            i += 1
        # 다른 경우
        else:
            # 접두사 길이가 0이 아니면
            if j != 0:
                # 최장접두사 끝 인덱스의 최장접두사 길이가 됨
                j = pi[j-1]
            # 접두사의 길이가 0이되면
            else:
                # 해당 인덱스에 최장접두사길이 0 넣고 다음인덱스로 넘어감
                pi[i] = 0
                i += 1

    return pi

def get_pi2(p: str):
    # j : 최장접두사의 길이
    j = 0
    # pi[i] : 현재 인덱스까지의 최장접두사의 길이
    pi = [0 for _ in range(len(p))]
    # i : 현재 인덱스 = 접미사의 끝
    for i in range(len(p)):
        # 접미사의 끝과 접두사의 끝이 다른 경우
        while j > 0 and p[i] != p[j]:
            j = pi[j-1]
        # 접미사의 끝과 접두사의 끝이 같은 경우
        if pi[i] == pi[j]:
            j += 1
            pi[i] = j

    return pi

# kmp 함수 구현
'''
i : s의 접미사 인덱스
j : p의 접두사 인덱스
1. s의 접미사와 p의 접두사가 같은경우
1-1. p의 접두사 인덱스가 p의 끝글자인 경우
     같은 글자 찾음. s의 시작인덱스 반환, p의 접두사 끝 인덱스로 설정   
1-2. 끝글자가 아니면 i, j 1 증가
2. s의 접미사 끝과 p의 접두사 끝이 다른경우
    같아질 때까지 바로이전 최대 접두사의 다음 인덱스로 돌아감    

1-1. 성공할 경우 종료
1-2. 실패할 경우 
    최대한 일치하는 인덱스 j를 찾는다
    pi[j]는 해당 인덱스에서 접두사의 최대길이
'''

def kmp(s: str, p: str):
    # 현재 p 인덱스
    j = 0
    pi = get_pi(p)
    ret = []
    for i in range(len(s)):
        # 현재 탐색점 i와 p의 접두사 끝 j가 다른 경우
        while j > 0 and s[i] != p[j]:
            # 바로 이전 p 인덱스까지의 접두사 끝 + 1 인덱스로 돌아감
            j = pi[j-1]
        # s의 끝과 p의 접두사 끝이 같은 경우
        if s[i] == p[j]:
            # p의 접두사 끝이 p의 마지막, 즉 p를 s에서 찾은 경우
            if j == len(p) - 1:
                 ret.append(i-len(p)+1)
                 # p의 마지막 인덱스에서 최장접두사 다음 인덱스부터 비교하면 된다
                 j = pi[j]
            else:
                j += 1

    return ret


print(kmp('fkasjdfhjksfhjdfkfjdffgsadf', 'jdf'))

print("time: ", time.time() - start)
