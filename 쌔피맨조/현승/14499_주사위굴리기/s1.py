import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, M, x, y, K = map(int, input().split())

dice = [[0, 0, 0] for _ in range(3)]

arr = [list(map(int, input().split())) for _ in range(N)]

orders = list(map(int, input().split()))

up_value = 0
for i in range(K):

    if orders[i] == 1:
        nx, ny = x, y + 1
        if not (0 <= nx < N and 0 <= ny < M):
            continue
        tmp = dice[1][0]
        dice[1][0] = dice[1][1]
        dice[1][1] = dice[1][2]
        dice[1][2] = up_value
        up_value = tmp
    elif orders[i] == 2:
        nx, ny = x, y - 1
        if not (0 <= nx < N and 0 <= ny < M):
            continue
        tmp = dice[1][2]
        dice[1][2] = dice[1][1]
        dice[1][1] = dice[1][0]
        dice[1][0] = up_value
        up_value = tmp
    elif orders[i] == 3:
        nx, ny = x - 1, y
        if not (0 <= nx < N and 0 <= ny < M):
            continue
        tmp = dice[2][1]
        dice[2][1] = dice[1][1]
        dice[1][1] = dice[0][1]
        dice[0][1] = up_value
        up_value = tmp
    else:
        nx, ny = x + 1, y
        if not (0 <= nx < N and 0 <= ny < M):
            continue
        tmp = dice[0][1]
        dice[0][1] = dice[1][1]
        dice[1][1] = dice[2][1]
        dice[2][1] = up_value
        up_value = tmp

    if arr[nx][ny]:
        dice[1][1] = arr[nx][ny]
        arr[nx][ny] = 0
    else:
        arr[nx][ny] = dice[1][1]
    x, y = nx, ny

    print(up_value)