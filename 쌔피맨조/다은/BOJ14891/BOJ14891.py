import sys
from pandas import DataFrame
sys.stdin = open("input.txt", "r")

#      0
#   7     1
#  6       2
#   5     3
#      4

def rotate(number, dir):
    # 시계방향 회전
    if dir == 1:
        k = gear[number].pop()
        gear[number].insert(0, k)
    # 반시계방향 회전
    if dir == -1:
        k = gear[number].pop(0)
        gear[number].append(k)


def what_rotate(num, dir):
    # 회전 방향을 미리 작성
    go_rotate = [0, 0, 0, 0, 0]
    go_rotate[num] = dir

    old_L = old_R = num
    old_L_dir = old_R_dir = dir

    for i in range(1, 4):
        # 회전안했으면 dir은 0
        L, L_dir = num - i, 0
        R, R_dir = num + i, 0

        # 범위 내이고, 이전 톱니바퀴가 회전했을 때, 현재 톱니바퀴도 회전해야할 때면 회전
        if L >= 1 and go_rotate[old_L] and gear[L][2] != gear[old_L][6]:
            L_dir = -1 * old_L_dir
            go_rotate[L] = L_dir
        old_L, old_L_dir = L, L_dir

        # 범위 내이고, 이전 톱니바퀴가 회전했을 때, 현재 톱니바퀴도 회전해야할 때면 회전
        if R <= 4 and go_rotate[old_R] and gear[R][6] != gear[old_R][2]:
            R_dir = -1 * old_R_dir
            go_rotate[R] = R_dir
        old_R, old_R_dir = R, R_dir

    for idx, idx_dir in enumerate(go_rotate):
        rotate(idx, idx_dir)


# 톱니바퀴 번호 1 ~ 4
# 회전시킬 방법의 수 K // [톱니바퀴 번호, 1이면 시계, -1이면 반시계]
gear = [0] + [list(input()) for _ in range(4)]
K = int(input())
IN = [list(map(int, input().split())) for _ in range(K)]

for num, dir in IN:
    what_rotate(num, dir)

print(int(gear[1][0])*1 + int(gear[2][0])*2 + int(gear[3][0])*4 + int(gear[4][0])*8)