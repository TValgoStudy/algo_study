import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame


# 상 우 하 좌 (시계 방향)
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def cal_score(r, c):
    check = [[0]*M for _ in range(N)]
    check[r][c] = 1
    B, C = IN[r][c], 1
    q = [(r, c)]
    while q:
        r, c = q.pop(0)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and not check[nr][nc] and IN[nr][nc] == B:
                check[nr][nc] = 1
                q.append((nr, nc))
                C += 1
    return B, C


def cal_dice(go, dice):
    if go == 0:     # 상
        next_dice = [dice[3], dice[0], dice[1], dice[2], dice[4], dice[5]]
    elif go == 1:   # 우
        next_dice = [dice[0], dice[5], dice[2], dice[4], dice[1], dice[3]]
    elif go == 2:   # 하
        next_dice = [dice[1], dice[2], dice[3], dice[0], dice[4], dice[5]]
    else:           # 좌
        next_dice = [dice[0], dice[4], dice[2], dice[5], dice[3], dice[1]]
    return next_dice


N, M, K = map(int, input().split())
IN = [list(map(int, input().split())) for _ in range(N)]

dice = [5, 6, 2, 1, 4, 3]
DIR, bottom = 1, 6
r, c = 0, 0
score = 0

while K:

    # 1. 주사위가 이동 방향으로 한 칸 굴러간다.
    nr = r + dr[DIR]
    nc = c + dc[DIR]
    if 0 <= nr < N and 0 <= nc < M:
        K -= 1
        r, c = nr, nc
        dice = cal_dice(DIR, dice)
        bottom = dice[1]
    else:
        DIR = (DIR + 2) % 4
        continue

    # 2. 주사위가 도착한 칸에 대한 점수를 획득
    B, C = cal_score(r, c)
    score += B * C

    # 3. 주사위 아랫 면에 있는 정수와 칸에 있는 정수를 비교하여 다음 방향을 정한다.
    if bottom > B:
        DIR = (DIR + 1) % 4
    elif bottom < B:
        DIR = (DIR - 1) % 4
    print(dice, bottom, DIR)

print(score)


  5
6 3 1
  2
  4

  3
6 2 1
  4
  5

# 예제 7
#   5
# 1 4 6
#   2
#   3
#
# 예제 7 밑면 가운데로 옮김
#   2
# 1 3 6
#   5
#   4
#
# 예제 8 밑면 가운데
#   2
# 3 6 4
#   5
#   1
# 예제 9 밑면 가운데
#   6
# 3 5 4
#   1
#   2
