import sys
sys.stdin = open('input.txt')

N = int(input())

alphaList = {}
NumList = []
result = 0
n = 9


for _ in range(N):
    s = input()
    SL = len(s)
    for i in range(SL):
        alphaList[s[i]] = alphaList.get(s[i], []) + [SL-i]


for key, valList in alphaList.items():
    valList = sorted(list(set(valList)), reverse=True)
    L = len(valList)

    valList.extend([0]*(8-L))
    valList.append(key)
    NumList.append(valList)

print(alphaList)

NumList.sort(reverse=True)
print(NumList)


for num in NumList:
    for jari in alphaList[num[-1]]:
        result += 10**(jari-1)*n
    n -= 1

print(result)
