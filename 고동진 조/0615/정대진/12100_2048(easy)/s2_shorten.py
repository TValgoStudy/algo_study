import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
Board = [list(map(int, input().split())) for _ in range(N)]
max_ = 0

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
condition = [lambda x, y: x > 0, lambda x, y: x < N - 1, lambda x, y: y > 0, lambda x, y: y < N - 1]
i_range = [range(1, N), range(N-2, -1, -1), range(N), range(N)]
j_range = [range(N), range(N), range(1, N), range(N-2, -1, -1)]


def move_block(d, board):
    global dr, dc, N, condition, i_range, j_range
    visited = [[0]*N for _ in range(N)]
    for i in i_range[d]:
        for j in j_range[d]:
            if board[i][j] == 0:
                continue
            row = i
            col = j
            while condition[d](row, col):
                nr = row + dr[d]
                nc = col + dc[d]
                if board[nr][nc] == 0:
                    board[nr][nc], board[row][col] = board[row][col], board[nr][nc]
                elif board[nr][nc] == board[row][col] and visited[nr][nc] == 0:
                    board[nr][nc], board[row][col] = board[nr][nc] + board[row][col], 0
                    visited[nr][nc] = 1
                    break
                else:
                    break
                row = nr
                col = nc

    return board


def brute_force(board, depth=0):
    global max_, N
    if depth == 5:
        tmp = 0
        for i in range(N):
            for j in range(N):
                if tmp < board[i][j]:
                    tmp = board[i][j]
        if tmp > max_:
            max_ = tmp
        return

    for d in range(4):
        # deepcopy
        duplicated_board = []
        for i in range(len(board)):
            duplicated_board.append(board[i][:])
        # 이동
        duplicated_board = move_block(d, duplicated_board)
        if board != duplicated_board:
            brute_force(duplicated_board, depth=depth+1)


brute_force(Board)
if max_ == 0:
    tmp = 0
    for i in range(N):
        for j in range(N):
            if tmp < Board[i][j]:
                tmp = Board[i][j]
    if tmp > max_:
        max_ = tmp
print(max_)
