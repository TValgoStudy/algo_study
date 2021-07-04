import sys
sys.stdin = open('input.txt')

# 4624ms
N = int(input())

for i in range(N):
    x, y, z = map(int, input().split())

    if i == 0:
        minArr = [x, y, z]
        maxArr = [x, y, z]
        continue

    a, b, c = minArr
    minArr[0] = x + min(a, b)
    minArr[1] = y + min(a, b, c)
    minArr[2] = z + min(b, c)

    a, b, c = maxArr
    maxArr[0] = x + max(a, b)
    maxArr[1] = y + max(a, b, c)
    maxArr[2] = z + max(b, c)


print(max(maxArr), min(minArr))