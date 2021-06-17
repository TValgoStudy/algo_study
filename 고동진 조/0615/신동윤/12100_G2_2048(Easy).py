import sys
sys.stdin = open('input.txt', 'r')


def inrange(r: int, c: int):
    return 0 <= r < N and 0 <= c < N


def plus(r: int, c: int, dir: int, board: list, visited: list):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    nr = r + dr[dir]
    nc = c + dc[dir]
    while True:
        if not inrange(nr, nc):
            if r == nr - dr[dir] and c == nc - dc[dir]:
                break

            board[nr - dr[dir]][nc - dc[dir]] = board[r][c]
            board[r][c] = 0
            break

        if board[nr][nc]:
            if board[nr][nc] == board[r][c] and not visited[nr][nc]:
                board[nr][nc] *= 2
                board[r][c] = 0
                visited[nr][nc] = 1
            else:
                if r == nr - dr[dir] and c == nc - dc[dir]:
                    break

                board[nr - dr[dir]][nc - dc[dir]] = board[r][c]
                board[r][c] = 0
            break

        nr += dr[dir]
        nc += dc[dir]


def move(dir: int, board: list):
    # 상 하 좌 우
    # 0  1  2  3
    if dir == 0:
        for c in range(N):
            visited = [[0 for _ in range(N)] for _ in range(N)]
            for r in range(N):
                if board[r][c]:
                    plus(r, c, dir, board, visited)
    elif dir == 1:
        for c in range(N):
            visited = [[0 for _ in range(N)] for _ in range(N)]
            for r in range(N - 1, -1, -1):
                if board[r][c]:
                    plus(r, c, dir, board, visited)
    elif dir == 2:
        for r in range(N):
            visited = [[0 for _ in range(N)] for _ in range(N)]
            for c in range(N):
                if board[r][c]:
                    plus(r, c, dir, board, visited)
    elif dir == 3:
        for r in range(N):
            visited = [[0 for _ in range(N)] for _ in range(N)]
            for c in range(N - 1, -1, -1):
                if board[r][c]:
                    plus(r, c, dir, board, visited)


def dfs(cases: list):
    global max_num
    board_copy = [[board[r][c] for c in range(N)] for r in range(N)]
    for case in cases:
        move(case, board_copy)

    max_num = max(max_num, max(sum(board_copy, [])))


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
max_num = 0

for i in range(4):
    for j in range(4):
        for k in range(4):
            for t in range(4):
                for u in range(4):
                    dfs([i, j, k, t, u])

print(max_num)


