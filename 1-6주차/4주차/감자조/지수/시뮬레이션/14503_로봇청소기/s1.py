import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]


# 상 우 하 좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def RobotGo(r, c, d, cnt, cantgo):
    if cantgo > 3:
        back_r, back_c = r - dr[d], c - dc[d]
        if arr[back_r][back_c] != 1:
            return RobotGo(back_r, back_c, d, cnt, 0)
        else:
            return cnt

    # 2
    left = d - 1
    if left == -1:
        left = 3

    if arr[r + dr[left]][c + dc[left] ] == 0:
        return RobotClean(r + dr[left], c + dc[left], left, cnt, 0) # 1번으로

    return RobotGo(r, c, left, cnt, cantgo+1)



def RobotClean(r, c, d, cnt, cantgo): # 1
    arr[r][c] = 2 # 1
    return RobotGo(r, c, d, cnt+1, 0)



print(RobotClean(r, c, d, 0, 0))



