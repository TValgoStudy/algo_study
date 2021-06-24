import math


arr = [0]*4
T = int(input())
for _ in range(T):
    N = int(input())
    cnt = 0
    arr[3] = N//3
    arr[2] = (N - arr[3]*3)//2
    arr[1] = N - arr[2]*2 - arr[3]*3
    while arr[3] != -1:
        while arr[2] != 0:
            cnt += math.factorial(sum(arr))//(math.factorial(arr[1])*math.factorial(arr[2])*math.factorial(arr[3]))
            arr[2] -= 1
            arr[1] += 2
        cnt += math.factorial(sum(arr))//(math.factorial(arr[1])*math.factorial(arr[2])*math.factorial(arr[3]))
        arr[3] -= 1
        arr[2] = (N - arr[3]*3)//2
        arr[1] = N - arr[2]*2 - arr[3]*3
    print(cnt)