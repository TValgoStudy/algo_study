import sys

r, c, y, x, n = map(int, sys.stdin.readline().strip().split(' '))

mapa = [list(map(int, sys.stdin.readline().strip().split(' '))) for _ in range(r)]

moves = list(map(int, sys.stdin.readline().strip().split(' ')))

dy, dx = [0, 0, 0, -1, 1], [0, 1, -1, 0, 0]  # first values are dummies

dice = [0] * 6

for move in moves:
    ny, nx = y + dy[move], x + dx[move]

    if 0 <= ny <= r - 1 and 0 <= nx <= c - 1:
        y, x = ny, nx

        if move == 4:
            dice[1], dice[5], dice[4], dice[0] = dice[0], dice[1], dice[5], dice[4]
        elif move == 3:
            dice[4], dice[5], dice[1], dice[0] = dice[0], dice[4], dice[5], dice[1]
        elif move == 2:
            dice[2], dice[5], dice[3], dice[0] = dice[0], dice[2], dice[5], dice[3]
        else:
            dice[3], dice[5], dice[2], dice[0] = dice[0], dice[3], dice[5], dice[2]

        item = mapa[y][x]

        if item == 0:
            mapa[y][x] = dice[0]
        else:
            dice[0] = item
            mapa[y][x] = 0

        print(dice[5])
    else:
        pass