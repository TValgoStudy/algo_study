# 최대 5번 이동시켜서 얻을 수 있는 가장 큰 블록을 출력한다
# brute force
# 상, 하, 좌, 우 4번 이동 가능
# 최대 다섯 번 이동 == 4 ** 5 == 2**10
import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
Board = [list(map(int, input().split())) for _ in range(N)]
max_ = 0


def move_block(i, board):
    # 0 up, 1 down, 2 left, 3 right
    used = [[False]*len(board) for _ in range(len(board))]
    if i == 0:
        for i1 in range(1, len(board)):
            for j1 in range(len(board)):
                i = i1
                j = j1
                if board[i][j] == 0:
                    continue
                while i > 0:
                    if board[i-1][j] == 0:
                        board[i-1][j], board[i][j] = board[i][j], 0
                    elif board[i-1][j] == board[i][j] and not used[i-1][j]:
                        board[i-1][j] += board[i][j]
                        board[i][j] = 0
                        used[i-1][j] = 1
                        break
                    else:
                        break
                    i -= 1
    # down
    elif i == 1:
        for i1 in range(len(board)-2, -1, -1):
            for j1 in range(len(board)):
                i = i1
                j = j1
                if board[i][j] == 0:
                    continue
                while i < len(board) - 1:
                    if board[i+1][j] == 0:
                        board[i+1][j], board[i][j] = board[i][j], 0
                    elif board[i+1][j] == board[i][j] and not used[i+1][j]:
                        board[i+1][j] += board[i][j]
                        board[i][j] = 0
                        used[i+1][j] = 1
                        break
                    else:
                        break
                    i += 1
    # left
    elif i == 2:
        for i1 in range(len(board)):
            for j1 in range(1, len(board)):
                i = i1
                j = j1
                if board[i][j] == 0:
                    continue
                while j > 0:
                    if board[i][j-1] == 0:
                        board[i][j-1], board[i][j] = board[i][j], 0
                    elif board[i][j-1] == board[i][j] and not used[i][j-1]:
                        board[i][j-1] += board[i][j]
                        board[i][j] = 0
                        used[i][j-1] = 1
                        break
                    else:
                        break
                    j -= 1
    # right
    else:
        for i1 in range(len(board)):
            for j1 in range(len(board)-2, -1, -1):
                i = i1
                j = j1
                if board[i][j] == 0:
                    continue
                while j < len(board) - 1:
                    if board[i][j+1] == 0:
                        board[i][j+1], board[i][j] = board[i][j], 0
                    elif board[i][j+1] == board[i][j] and not used[i][j+1]:
                        board[i][j+1] += board[i][j]
                        board[i][j] = 0
                        used[i][j+1] = 1
                        break
                    else:
                        break
                    j += 1

    return board


# N은 최대 20 -> 400, 메모리 400 * 1024 약 400000
def brute_force(board, depth=0):
    global max_
    if depth == 5:
        tmp = 0
        for i in range(len(board)):
            for j in range(len(board[i])):
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
print(max_)
