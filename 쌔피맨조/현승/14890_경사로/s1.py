import sys
sys.stdin = open("input.txt", "r")
# input = sys.stdin.readline

N, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for i in range(N):
    h = arr[i][0]
    cnt = 1
    for j in range(1, N):
        if h == arr[i][j]:
            cnt += 1
        elif h + 1 == arr[i][j] and cnt >= L:
            cnt = 1
            h += 1
        else:
            break
    else:
        ans += 1
        print(i, '행')
        continue

    h = arr[i][N-1]
    cnt = 1
    for j in range(N-2, -1, -1):
        if h == arr[i][j]:
            cnt += 1
        elif h + 1 == arr[i][j] and cnt >= L:
            cnt = 1
            h += 1
        else:
            break
    else:
        ans += 1
        print(i, '행')

for i in range(N):
    h = arr[0][i]
    cnt = 1
    for j in range(1, N):
        if h == arr[j][i]:
            cnt += 1
        elif h + 1 == arr[j][i] and cnt >= L:
            cnt = 1
            h += 1
        else:
            break
    else:
        ans += 1
        print(i, '열')
        continue

    h = arr[N-1][i]
    cnt = 1
    for j in range(N - 2, -1, -1):
        if h == arr[j][i]:
            cnt += 1
        elif h + 1 == arr[j][i] and cnt >= L:
            cnt = 1
            h += 1
        else:
            break
    else:
        ans += 1
        print(i, '열')

print(ans)