import sys
sys.stdin = open('input.txt', 'r')


from collections import deque


def inrange(r: int, c: int) -> bool:
    return 0 <= r < N and 0 <= c < N


def gravity():
    for c in range(N):
        stack = []
        for r in range(N):
            if board[r][c] == -1:
                stack = []
            elif board[r][c] == -2:
                L = len(stack)
                for i in range(L):
                    board[r - i][c] = stack[L - 1 - i]
                    board[r - i - 1][c] = -2
            else:
                stack.append(board[r][c])


def find_group(row: int, col: int) -> list:
    dr = [0, 0, -1, 1]
    dc = [1, -1, 0, 0]
    Q = deque([[row, col]])
    visited = [[0 for _ in range(N)] for _ in range(N)]
    color = board[row][col]
    group = [[row, col]]
    cnt = 0

    visited[row][col] = 1
    while Q:
        r, c = Q.popleft()
        already_set.add((r, c))
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if inrange(nr, nc) and not visited[nr][nc]:
                if board[nr][nc] == color or board[nr][nc] == 0:
                    visited[nr][nc] = 1
                    Q.append([nr, nc])
                    group.append([nr, nc])
                    if board[nr][nc] == 0:
                        cnt += 1

    group.append(cnt)
    if len(group) < 3:
        group = []

    return group


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

answer = 0

while True:
    already_set = set()
    max_val = []
    for r in range(N):
        for c in range(N):
            if board[r][c] > 0:
                if (r, c) in already_set: continue
                temp = find_group(r, c)
                if len(temp) == 0: continue

                if len(temp) > len(max_val):
                    max_val = temp
                elif len(temp) == len(max_val) and max_val[-1] <= temp[-1]:
                    max_val = temp

    if len(max_val) == 0:
        break

    answer += (len(max_val) - 1) ** 2
    for i in range(len(max_val) - 1):
        r, c = max_val[i]
        board[r][c] = -2

    gravity()
    board = [list(i) for i in zip(*board)][::-1] # 반시계 90도 회전
    gravity()

print(answer)