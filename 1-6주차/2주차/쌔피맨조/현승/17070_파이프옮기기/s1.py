import sys
sys.stdin = open("input.txt", "r")

def dfs(second, d):
    global answer

    if second == (N-1, N-1):
        answer += 1
        return

    x, y = second

    for dx, dy, d in direction_dict[d]:
        nx = x + dx
        ny = y + dy
        if not (0 <= nx < N and 0 <= ny < N):
            continue
        if arr[nx][ny] == 1:
            continue
        if (dx, dy) == (1, 1):
            if arr[nx-1][ny] == 1 or arr[nx][ny-1] == 1:
                continue
        arr[nx][ny] = 1
        dfs((nx, ny), d)
        arr[nx][ny] = 0


N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]
direction_dict = {
        # 가로
        0: [(1, 1, 2), (0, 1, 0)],
        # 세로
        1: [(1, 1, 2), (1, 0, 1)],
        # 대각선
        2: [(1, 1, 2), (1, 0, 1), (0, 1, 0)]
    }
answer = 0
if arr[N-1][N-1] == 1:
    answer = 0
else:
    dfs((0, 1), 0)
print(answer)

