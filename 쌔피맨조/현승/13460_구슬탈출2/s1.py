import sys
sys.stdin = open("input.txt", "r")
from pprint import pprint
# 빨간 구술이 파란구술에 막힐 수 있을까?
# '구슬은 한 칸을 모두 차지한다.
# 일단 1. 빨간 구슬이 파란구슬에 닿으면 막히는 걸로 구현해보자

def dfs(red_x, red_y, blue_x, blue_y, cnt):
    global ans

    # 종료 조건 : 둘다 움직일 수 없거나 구멍에 빠지거나 카운트가 11이 됐을 때
    if cnt > 10 or arr[blue_x][blue_y] == 'O':
        return
    # 가지치기
    if cnt > ans:
        return
    # 성공 시 카운트 갱신
    if arr[red_x][red_y] == 'O':
        if ans > cnt:
            ans = cnt

    for dx, dy, dir_idx in [(-1, 0, 0), (1, 0, 1), (0, -1, 2), (0, 1, 3)]:
        red_nx, red_ny = red_x + dx, red_y + dy
        blue_nx, blue_ny = blue_x + dx, blue_y + dy
        red_cnt, blue_cnt = 0, 0
        # 주어진 방향으로 끝까지
        while arr[red_nx][red_ny] == '.':
            red_nx += dx
            red_ny += dy
            red_cnt += 1
        while arr[blue_nx][blue_ny] == '.':
            blue_nx += dx
            blue_ny += dy
            blue_cnt += 1
        # 벽에 도달했으면 한 칸 후진
        if arr[red_nx][red_ny] == '#':
            red_nx -= dx
            red_ny -= dy
        if arr[blue_nx][blue_ny] == '#':
            blue_nx -= dx
            blue_ny -= dy

        # 만약 두 좌표가 같아졌다면 원래 뒤에 있던애가 뒤로 후진(후진 불가면 return)
        if red_nx == blue_nx and red_ny == blue_ny and arr[red_nx][red_ny] != 'O':
            if red_cnt >= blue_cnt:
                red_nx -= dx
                red_ny -= dy
            else:
                blue_nx -= dx
                blue_ny -= dy

        # 방문기록 체크
        if red_check[dir_idx][red_nx][red_ny] and blue_check[dir_idx][blue_nx][blue_ny]:
            continue
        # 상태 저장
        red_status, blue_status = red_check[dir_idx][red_nx][red_ny], blue_check[dir_idx][blue_nx][blue_ny]
        # 방문 기록 체크
        red_check[dir_idx][red_nx][red_ny] = 1
        blue_check[dir_idx][blue_nx][blue_ny] = 1
        # dfs
        dfs(red_nx, red_ny, blue_nx, blue_ny, cnt + 1)
        # 방문 기록 해제
        red_check[dir_idx][red_nx][red_ny] = red_status
        blue_check[dir_idx][blue_nx][blue_ny] = blue_status


N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]

red_x, red_y = 0, 0
blue_x, blue_y = 0, 0
for i in range(1, N-1):
    for j in range(1, M-1):
        if arr[i][j] == 'B':
            arr[i][j] = '.'
            blue_x, blue_y = i, j
        elif arr[i][j] == 'R':
            arr[i][j] = '.'
            red_x, red_y = i, j

# pprint(arr)
# 0 1 2 3 : 상 하 좌 우
red_check = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(4)]
blue_check = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(4)]

ans = 11
dfs(red_x, red_y, blue_x, blue_y, 0)

if ans == 11:
    ans = -1

print(ans)