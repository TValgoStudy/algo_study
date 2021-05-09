import sys
sys.stdin = open("input.txt", "r")

def dfs(x, y, d):
    global answer

    if (x, y) == (N-1, N-1):
        answer += 1
        return

    if d == 0 or d == 2:
        if y + 1 < N:
            if arr[x][y+1] == 0:
                dfs(x, y+1, 0)
    if d == 1 or d == 2:
        if x + 1 < N:
            if arr[x+1][y] == 0:
                dfs(x+1, y, 1)
    if d == 0 or d == 1 or d == 2:
        if x + 1 < N and y + 1 < N:
            if arr[x+1][y] == 0 and arr[x][y+1] == 0 and arr[x+1][y+1] == 0:
                dfs(x+1, y+1, 2)

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

answer = 0
dfs(0, 1, 0)

print(answer)