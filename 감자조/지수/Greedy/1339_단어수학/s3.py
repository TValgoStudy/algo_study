import sys
sys.stdin = open('input.txt')

# 자릿수가 다른 경우
# ACDEB
# 00GCF
# 자릿수가 큰걸 무조건 큰 숫자로?
# 10000*A + (1000+10)*C + 100*G + 100*D + 10*E + 1*B + 1*F

# 76ms

N = int(input())

alphaList = {}
numList = []
result = 0
n = 9

for _ in range(N):
    s = input()
    SL = len(s)
    for i in range(SL):
        alphaList[s[i]] = alphaList.get(s[i], 0) + 10**(SL-i-1)


for key, val in alphaList.items():
    numList.append((val, key))
numList.sort(reverse=True)


for chasu, gyesu in numList:
    result += chasu * n
    n -= 1

print(result)


