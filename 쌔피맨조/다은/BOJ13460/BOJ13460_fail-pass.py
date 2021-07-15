import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame


# 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def move(go_dir, K, IN):
    r, c = K[0]
    color = K[1]
    while 1:
        nr = r + dr[go_dir]
        nc = c + dc[go_dir]
        if 0 <= nr < N and 0 <= nc < M:
            if IN[nr][nc] == 'O':
                # IN[r][c] = '.' 이 부분 안 써서 틀림
                IN[r][c] = '.'
                return ('goal', color)
            elif IN[nr][nc] != '.':
                IN[r][c] = color
                break
            IN[r][c] = '.'
            r, c = nr, nc
        else:
            break
    return ((r, c), color)


def func(DIR: list, B: tuple, R: tuple, IN: list):
    global result
    go_dir = DIR[-1]  # 0~3
    if result <= len(DIR):
        return

    go1, go2 = (B, 'B'), (R, 'R')
    if go_dir == 0:
        # 똑같은 열에서 // B가 더 밑에 있으면 R 먼저 굴리기
        if B[1] == R[1]:
            if B[0] > R[0]:
                go1, go2 = (R, 'R'), (B, 'B')
    elif go_dir == 1:
        # 똑같은 열에서 // R이 더 밑에 있으면 R 먼저 굴리기
        if B[1] == R[1]:
            if B[0] < R[0]:
                go1, go2 = (R, 'R'), (B, 'B')
    elif go_dir == 2:
        # 똑같은 행에서 // R이 더 왼쪽이면 R 먼저 굴리기
        if B[0] == R[0]:
            if B[1] > R[1]:
                go1, go2 = (R, 'R'), (B, 'B')
    elif go_dir == 3:
        # 똑같은 행에서 // R이 더 오른쪽이면 R 먼저 굴리기
        if B[0] == R[0]:
            if B[1] < R[1]:
                go1, go2 = (R, 'R'), (B, 'B')
    go1 = move(go_dir, go1, IN)
    go2 = move(go_dir, go2, IN)

    if go1[0] == 'goal' and go2[0] == 'goal':
        return
    elif go1[0] == 'goal':
        if go1[1] == 'R':
            if result > len(DIR):
                result = len(DIR)
        return
    elif go2[0] == 'goal':
        if go2[1] == 'R':
            if result > len(DIR):
                result = len(DIR)
        return

    for k in range(4):
        IN_copy2 = [i[:] for i in IN]
        if k != go_dir:
            # go1 = B , go2 = R
            if go1[1] == 'B':
                func(DIR + [k], go1[0], go2[0], IN_copy2)
            # go1 = R, go2 = B
            else:
                func(DIR + [k], go2[0], go1[0], IN_copy2)



N, M = map(int, input().split())
IN = [list(input()) for _ in range(N)]

B, R, hole = 0, 0, 0
for r in range(N):
    for c in range(M):
        if IN[r][c] == 'B':
            B = (r, c)
        elif IN[r][c] == 'R':
            R = (r, c)
        elif IN[r][c] == 'O':
            hole = (r, c)

result = 11
for i in range(4):
    IN_copy = [i[:] for i in IN]
    func([i], B, R, IN_copy)

print(-1) if result == 11 else print(result)