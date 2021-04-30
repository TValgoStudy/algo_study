import sys
sys.stdin = open("input.txt", "r")


def inrange(r, c):
    return 0 <= r < N and 0 <= c < N

N = int(input())
apple = int(input())
board = [[0]*N for _ in range(N)]
commands = []
for _ in range(apple):
    r, c = map(int, input().split())
    board[r-1][c-1] = 1

L = int(input())
for _ in range(L):
    command = input().split()
    commands.append(command)

tail = [0, 0]
head = [0, -1]
time = 0
dir = 0
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
path = [[0, 0]]
while True:
    pos_r, pos_c = head
    pos_r += dr[dir]
    pos_c += dc[dir]

    if not inrange(pos_r, pos_c) or (pos_r, pos_c) in path:
        break

    head = [pos_r, pos_c]
    path.append((pos_r, pos_c))
    if not board[pos_r][pos_c]:
        path.pop(0)
    else:
        board[pos_r][pos_c] = 0

    if commands:
        if int(commands[0][0]) == time:
            command = commands.pop(0)
            if command[1] == 'L':
                dir -= 1
                if dir < 0:
                    dir = 3
            elif command[1] == 'D':
                dir += 1
                if dir > 3:
                    dir = 0

    time += 1

print(time)


