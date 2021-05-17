import sys
sys.stdin = open("input.txt", "r")
import time
start = time.time()


import sys
input = sys.stdin.readline

def rotate(info, a):
    arr = [row[:] for row in a]
    r, c = (info[0] - info[2] - 1, info[1] - info[2] - 1)
    c_len = info[1] + info[2]-c
    r_len = info[0] + info[2]-r

    tmp = [[0 for _ in range(c_len)] for _ in range(r_len)]

    x, y = 0, 0
    while not tmp[x][y]:
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx = x + dx
            ny = y + dy
            while (0 <= nx < r_len and 0 <= ny < c_len) and not tmp[nx][ny]:
                tmp[nx][ny] = arr[x+r][y+c]
                x = nx
                y = ny
                nx += dx
                ny += dy
        x += 1
        y += 1

    for i in range(r_len):
        for j in range(c_len):
            if tmp[i][j]:
                arr[i+r][j+c] = tmp[i][j]

    return arr

def permutation(cnt, arr):
    global answer
    if cnt == K:
        for row in arr:
            answer = min(sum(row), answer)
        return

    for idx in range(K):
        if not visited[idx]:
            visited[idx] = True
            tmp = rotate(info[idx], arr)
            permutation(cnt + 1, tmp)
            visited[idx] = False

N, M, K = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(N)]
info = [list(map(int, input().split())) for _ in range(K)]
answer = 987654321

visited = [False for _ in range(K)]
permutation(0, A)


print(answer)




print("time: ", time.time() - start)