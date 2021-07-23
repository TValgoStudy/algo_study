import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def binarySearch(val, l, r):
    global answer

    if l > r:
        return

    m = (l + r) // 2
    total = val + arr2[1][m]

    if total > 0:
        binarySearch(val, l, m-1)
    elif total == 0:
        answer += 1
        return
    elif total < 0:
        binarySearch(val, m+1, r)



N = int(input())
arr1 = [[], [], [], []]
arr2 = [[], []]
answer = 0

for _ in range(N):
    temp = list(map(int, input().split()))
    for i in range(4):
        arr1[i].append(temp[i])

for i in range(2):
    for x in arr1[i*2]:
        for y in arr1[i*2+1]:
            arr2[i].append(x+y)

arr2[0].sort()
arr2[1].sort()
N = len(arr2[0])

for a in arr2[0]:
    binarySearch(a, 0, N-1)

print(answer)