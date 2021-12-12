import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame


score1 = [1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 0, 0, 0, 0, 0, 0]
score2 = [1, 0, 0, 0, 0,  0, 13, 16, 19, 25, 30, 35, 40,  0, 0, 0, 0, 0, 0]
score3 = [1, 0, 0, 0, 0,  0,  0,  0,  0,  0,  0, 22, 24, 25, 30, 35, 40, 0, 0, 0, 0, 0, 0]
score4 = [1, 0, 0, 0, 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, 28, 27, 26, 25, 30, 35, 40, 0, 0, 0, 0, 0, 0]

move_blue = [5, 10, 15]
matrix = [score1, score2, score3, score4]


def check(next, me):
    b, r = next
    for i, j in me:
        if matrix[i][j] == matrix[b][r]:
            if [i, j] == [0, 15] and b:
                continue
            elif [b, r] == [0, 15] and i:
                continue
            else:
                return True
    return False


def func(me, idx, my_sum):
    global result

    # 종료 조건
    if idx == N:
        if result < my_sum:
            result = my_sum
        return

    # 움직여야 하는 길이
    move = IN[idx]
    for i in range(4):
        me_copy = me[i][:]
        blue, red = me[i]
        # 만약 blue가 0이면 파란칸을 밟을 수 있다.
        if blue == 0:
            if red == 5:
                blue = 1
            elif red == 10:
                blue = 2
            elif red == 15:
                blue = 3
        red += move

        # 점수가 있는 곳에서 출발하는 거면 출발 or 도착점에 아무도 없거나 완전 도착이면 이동 가능
        if matrix[me[i][0]][me[i][1]] and ([blue, red] not in me or not matrix[blue][red]):
            if matrix[blue][red] in [25, 30, 35, 40] and check([blue, red], me):
                continue

            # me 갱신해서 재귀
            me[i] = [blue, red]
            func(me, idx + 1, my_sum + matrix[blue][red])
            # 원상복구
            me[i] = me_copy



IN = list(map(int, input().split()))
N = len(IN)

result = 0
me = [[0, 0], [0, 0], [0, 0], [0, 0]]    # blue 개수, red 개수
func(me, 0, 0)

print(result)
