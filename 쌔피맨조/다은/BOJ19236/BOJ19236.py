import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame


dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, -1, -1, -1, 0, 1, 1, 1]


def rotate(r, c, dir):
    while 1:
        nr = r + dr[dir]
        nc = c + dc[dir]
        if (0 <= nr < 4 and 0 <= nc < 4) and fish[nr][nc] != 99:
            break
        dir = (dir + 1) % 8
        fish_dir[r][c] = dir

    return nr, nc


def fish_move():
    # 1부터 16까지 순서대로 찾기
    for i in range(1, 17):
        flag = False
        for r in range(4):
            for c in range(4):
                # 물고기가 i 일 때
                if fish[r][c] == i:
                    # 다음 위치에 있는 거랑 교환
                    nr, nc = rotate(r, c, fish_dir[r][c])
                    fish[r][c], fish[nr][nc] = fish[nr][nc], fish[r][c]
                    fish_dir[r][c], fish_dir[nr][nc] = fish_dir[nr][nc], fish_dir[r][c]
                    flag = True
                if flag:
                    break
            if flag:
                break


def func(r, c, current_sum, fish, fish_dir):
    global result

    if result < current_sum:
        result = current_sum

    # 물고기 움직이기
    fish_move()

    # 상어 움직이기
    for k in range(1, 4):
        nr = r + dr[fish_dir[r][c]] * k
        nc = c + dc[fish_dir[r][c]] * k

        # 이동할 수 있고 물고기가 있으면
        if 0 <= nr < 4 and 0 <= nc < 4 and (fish[nr][nc] and fish[nr][nc] != 99):
            fish_copy = [i[:] for i in fish]
            fish_dir_copy = [i[:] for i in fish_dir]
            fish_copy[r][c], fish_copy[nr][nc] = 0, 99

            # 해당 위치를 가지고 재귀
            func(nr, nc, current_sum + tmp, fish_copy, fish_dir_copy)


fish = [[0]*4 for _ in range(4)]
fish_dir = [[0]*4 for _ in range(4)]
shark = 99

for r in range(4):
    tmp = list(map(int, input().split()))
    for i in range(4):
        fish[r][i] = tmp[2 * i]
        fish_dir[r][i] = tmp[2 * i + 1] - 1

# 첫번째 물고기 먹고 위치 차지
tmp = fish[0][0]
fish[0][0] = 99

result = 0
func(0, 0, tmp, fish, fish_dir)
print(result)
