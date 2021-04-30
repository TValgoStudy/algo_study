import sys
sys.stdin = open("input.txt", "r")

from collections import deque
def bfs():
    red_r, red_c = red
    blue_r, blue_c = blue
    visited = set()
    Q = deque([[red_r, red_c, blue_r, blue_c]])
    cnt = 1
    while Q:
        if cnt == 11:
            break

        L = len(Q)
        for _ in range(L):
            red_r, red_c, blue_r, blue_c = Q.popleft()
            for dir in ['R', 'L', 'U', 'D']:
                red_nr, red_nc, blue_nr, blue_nc = red_r, red_c, blue_r, blue_c
                find_red, find_blue, dist_red, dist_blue = 0, 0, 0, 0
                while board[red_nr+dr[dir]][red_nc+dc[dir]] in possible:
                    red_nr += dr[dir]
                    red_nc += dc[dir]
                    dist_red += 1

                    if board[red_nr][red_nc] == 'O':
                        find_red = 1
                        break

                while board[blue_nr+dr[dir]][blue_nc+dc[dir]] in possible:
                    blue_nr += dr[dir]
                    blue_nc += dc[dir]
                    dist_blue += 1

                    if board[blue_nr][blue_nc] == 'O':
                        find_blue = 1
                        break


                if red_nr == blue_nr and red_nc == blue_nc:
                    if dist_red > dist_blue:
                        red_nr -= dr[dir]
                        red_nc -= dc[dir]
                    else:
                        blue_nr -= dr[dir]
                        blue_nc -= dc[dir]

                if find_blue:
                    continue

                if find_red:
                    return cnt

                if not (red_nr, red_nc, blue_nr, blue_nc) in visited:
                    visited.add((red_nr, red_nc, blue_nr, blue_nc))
                    Q.append([red_nr, red_nc, blue_nr, blue_nc])
        cnt += 1

    return -1


min_val = 11
R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]
dr = {'R': 0, 'L': 0, 'U': -1, 'D': 1}
dc = {'R': 1, 'L': -1, 'U': 0, 'D': 0}
red = []
blue = []
possible = ['.', 'O']

for r in range(R):
    for c in range(C):
        if board[r][c] == 'R':
            red = [r, c]
            board[r][c] = '.'
        elif board[r][c] == 'B':
            blue = [r, c]
            board[r][c] = '.'

print(bfs())
