import sys
sys.stdin = open('input.txt')

q = lambda: list(map(int, sys.stdin.readline().split()))
m, n = q()
r, c, h = q()
mat = []
for _ in range(m):
    mat.append(q())

r_move = [0, -1, 0, 1]
c_move = [-1, 0, 1, 0]

b = 1
cnt = 1
mat[r][c] = -1

while b:
    for i in range(4):
        nr = r + r_move[h]
        nc = c + c_move[h]
        h = (h + 3) % 4

        if mat[nr][nc] == 0:
            mat[nr][nc] = -1
            r = nr
            c = nc
            cnt += 1
            check = 1
            break;
        else:
            check = 0

    if i == 3 and check == 0:
        nr = r + r_move[(h + 3) % 4]
        nc = c + c_move[(h + 3) % 4]
        if mat[nr][nc] == 1:
            b = 0
        else:
            r = nr
            c = nc
print(cnt)