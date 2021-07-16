import sys
sys.stdin = open('input.txt')

N = int(input())
broken = []
if int(input()) != 0:
    broken = list(map(int, input().split()))
available = [str(n) for n in range(10) if n not in broken]
available.sort()
maxDistance = abs(N - 100)
maxDistanceList = [maxDistance]
sN = str(N)
if len(available) == 0:
    print(maxDistance)
    exit()
if len(available) == 1 and available[0] == '0':
    maxDistanceList.append(N + 1)
    print(min(maxDistanceList))
    exit()


def findBS(findString, startIndex, resultString):
    if len(findString) <= startIndex:
        return resultString
    for i in available:
        if int(findString[0:startIndex+1]) <= int(resultString + i):
            r = findBS(findString, startIndex + 1, resultString + i)
            if r:
                return r
    if startIndex == 0:
        return findBS('0' + findString, startIndex, resultString)
    else:
        return None


def findSB(findString, startIndex, resultString):

    if len(findString) <= startIndex:
        return resultString

    for i in reversed(available):
        if int(findString[0:startIndex+1]) >= int(resultString + i):
            r = findSB(findString, startIndex + 1, resultString + i)
            if r:
                return r

    if startIndex == 0:
        return findSB(findString, startIndex + 1, resultString)
    else:
        return None


bs = findBS(sN, 0, '')
if bs:
    bs = str(int(bs))
    maxDistanceList.append(len(bs) + int(bs) - N)
sb = findSB(sN, 0, '')
if sb:
    sb = str(int(sb))
    maxDistanceList.append(len(sb) + N - int(sb))

print(min(maxDistanceList))