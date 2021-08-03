import sys
sys.stdin = open("input3.txt", "r")
from pandas import DataFrame

#  기본      남        북        동        서
#   0        1         3         0        0
# 4 1 5    4 2 5     4 0 5     1 5 3    3 4 1
#   2        3         1         2        2
#   3        0         2         4        5

def move(go, dice):
    if go == 1:   # 동
        next_dice = [dice[0], dice[5], dice[2], dice[4], dice[1], dice[3]]
    elif go == 2: # 서
        next_dice = [dice[0], dice[4], dice[2], dice[5], dice[3], dice[1]]
    elif go == 3: # 남
        next_dice = [dice[1], dice[2], dice[3], dice[0], dice[4], dice[5]]
    else:         # 북
        next_dice = [dice[3], dice[0], dice[1], dice[2], dice[4], dice[5]]
    return next_dice

N, M, x, y, K = map(int, input().split())
IN = [list(map(int, input().split())) for _ in range(N)]
DIR = list(map(int, input().split()))

dice = [0] * 6
r, c = x, y

drc = [0, (0, 1), (0, -1), (-1, 0), (1, 0)]
for i in range(K):
    go = DIR[i]
    nr, nc = r + drc[go][0], c + drc[go][1]
    # nr, nc가 맵 안이어서 움직일 수 있을 때
    if 0 <= nr < N and 0 <= nc < M:
        # 주사위를 굴린다.
        dice = move(go, dice)

        # 맵 안에 숫자가 쓰여있으면
        if IN[nr][nc]:
            # 칸에 쓰인 수가 주사위 바닥으로 복사하고 칸은 0
            dice[1] = IN[nr][nc]
            IN[nr][nc] = 0

        # 맵 안에 숫자가 안 쓰여 있으면
        else:
            # 주사위의 바닥면에 쓰인 수가 칸에 복사
            IN[nr][nc] = dice[1]
        r, c = nr, nc

        # 주사위 윗 면에 쓰인 수를 출력
        print(dice[3])
