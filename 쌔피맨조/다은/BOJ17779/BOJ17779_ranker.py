import sys
sys.stdin = open("input.txt", "r")

board = None
min_diff = 100*20*20
board_sum = 0

def calc(d1, d2, x, y):
    global board, min_diff, board_sum
    sums = [0, 0, 0, 0, 0]
    for i in range(x):
        sums[0] += sum(board[i][0:y+1])
        sums[1] += sum(board[i][y+1:])
    for i in range(d1):
        sums[0] += sum(board[x+i][0:y-i])
        sums[3] += sum(board[x+d1+d2-i][y-d1+d2+1+i:])
    for i in range(d2+1):
        sums[1] += sum(board[x+i][y+1+i:])
        sums[2] += sum(board[x+d1+d2-i][0:y-d1+d2-i])
    for i in range(x+d1+d2+1,len(board)):
        sums[2] += sum(board[i][0:y-d1+d2])
        sums[3] += sum(board[i][y-d1+d2:])
    sums[4] = board_sum - sum(sums[0:4])
    diff = max(sums)-min(sums)
    if diff < min_diff:
        min_diff = diff

def bj17779():
    global board, min_diff, board_sum
    n = int(input())
    board = [list(map(int, input().split(' '))) for _ in range(n)]
    for b in board:
        for v in b:
            board_sum += v
    for d1 in range(1, n-1):
        for d2 in range(1, n-d1):
            for x in range(0, n-d1-d2):
                for y in range(d1, n-d2):
                    calc(d1, d2, x, y)
    print(min_diff)

bj17779()
