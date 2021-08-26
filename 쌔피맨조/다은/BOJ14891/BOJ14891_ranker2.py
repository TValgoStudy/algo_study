import sys
read = sys.stdin.readline

gears = []
for _ in range(4):
    gears.append(read().strip())


def rotate(target, num, spin, left, right):
    # 왼쪽, 오른쪽 톱니바퀴 선택 + left/right : 어느 방향을 볼건지
    left_target, right_target = False, False
    if left:
        if num > 0 and num <= 3:
            left_target = gears[num-1]
        else:
            left = False
    if right:
        if num >= 0 and num < 3:
            right_target = gears[num+1]
        else:
            right = False

    # 맞닿은 부분이 다르면 반대방향으로, 어느 방향을 볼 건지 선택
    if left_target and left_target[2] != target[6]:
        rotate(left_target, num-1, -spin, True, False)
    if right_target and right_target[6] != target[2]:
        rotate(right_target, num+1, -spin, False, True)

    # 회전
    if spin == 1:
        gears[num] = target[-1] + target[0:-1]
    else:
        gears[num] = target[1::] + target[0]


for i in range(int(read())):
    num, spin = map(int, read().split())
    rotate(gears[num-1], num-1, spin, True, True)
ans = ''
for i in range(3, -1, -1):
    ans += gears[i][0]

print(int(ans, 2))
