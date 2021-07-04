import sys
sys.stdin = open('input.txt')

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

minArr = [[0] * 3 for _ in range(N)]
maxArr = [[0] * 3 for _ in range(N)]

minArr[0] = maxArr[0] = arr[0]

for i in range(1, N):
    minArr[i][0] = arr[i][0] + min(minArr[i-1][0], minArr[i-1][1])
    maxArr[i][0] = arr[i][0] + max(maxArr[i - 1][0], maxArr[i - 1][1])

    minArr[i][1] = arr[i][1] + min(minArr[i - 1][0], minArr[i - 1][1], minArr[i - 1][2])
    maxArr[i][1] = arr[i][1] + max(maxArr[i - 1][0], maxArr[i - 1][1], maxArr[i - 1][2])

    minArr[i][2] = arr[i][2] + min(minArr[i - 1][1], minArr[i - 1][2])
    maxArr[i][2] = arr[i][2] + max(maxArr[i - 1][1], maxArr[i - 1][2])

print(max(maxArr[-1]), min(minArr[-1]))