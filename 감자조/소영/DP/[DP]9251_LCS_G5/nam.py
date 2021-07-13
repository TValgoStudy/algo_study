import sys

sys.stdin = open('input.txt', 'r')

def s():
    s1, s2 = input(), input() # 문자열 받아옴
    dp = [0] * 1000 # 최대 글자수 1000
    for i in range(len(s1)): # 첫 문자열 만큼 돌거고
        max_dp = 0 # 시작 자리수 바뀔때마다 리셋
        for j in range(len(s2)): # 두번째 문자열 순회
            if max_dp < dp[j]: # 최대dp값이 비교 j dp값보다 크면
                max_dp = dp[j] # 갱신
            elif s1[i] == s2[j]: # 같으면
                dp[j] = max_dp + 1 # 추가
            print(max_dp, dp)
    print(max(dp))
s()

####
# 예시
# ACD, ABC
# (i=0) A A : dp= [1, 0, 0] = 1, A B : dp = [1, 0, 0], A C : db = [1, 0, 0], max_dp = 0
# (i=1) C A : max_dp = 1, dp =[1, 0, 0], C B : dp = [1, 0, 0], C C : dp = [1, 0, 2]
# (i=2) D A : max_dp = 2, dp =[1, 0, 2], D B : dp = [1, 0, 2], D C : dp = [1, 0, 2]

