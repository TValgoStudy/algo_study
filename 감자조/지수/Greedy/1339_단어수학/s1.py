import sys
sys.stdin = open('input.txt')

# 자릿수가 다른 경우
# ACDEB
# 00GCF
# 자릿수가 큰걸 무조건 큰 숫자로?
# 10000*A + 1000*C + 100*(G+D) + 10*(E+C) + 1*(B+F)

# 자릿수가 동일한 경우?
# ABD
# DAF
# A를 9로 두는게 더 큼

N = int(input())

numList = [[] for _ in range(8)]
alphaList = {}
alphaToNum = {}

for _ in range(N):
    s = input()
    SL = len(s)
    alphaToNum[s] = 0
    for i in range(SL):
        numList[SL-i-1].append(s[i])
        alphaToNum[s[i]] = 0
        alphaList[s[i]] = alphaList.get(s[i], []) + [SL-i-1]

num = 9
MAX = 0
print(alphaList)

# for i in range(7, -1, -1):
#     if numList[i] == 0:
#         continue
#
#     if len(numList[i]) == 1:
#         if alphaToNum[numList[i][0]]:
#             continue
#         alphaToNum[numList[i][0]] = num
#         num -= 1
#     else:
#
#         print(alphaList)



