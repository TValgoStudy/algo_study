import sys
from collections import deque

#https://chldkato.tistory.com/54

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

# 좌 우 하 상
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 상어 위치 저장할 변수
sx, sy = 0, 0

# 상어 위치 찾아서 저장!
for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            arr[i][j] = 0
            sx, sy = i, j
            break
# 시작 사이즈
size = 2
# 움직인 수
move_num = 0
# 먹은 수
eat = 0


while True:
    q = deque()
    # q에 넣음
    q.append((sx, sy, 0))
    # 방문 체크
    visited = [[False] * n for _ in range(n)]
    flag = 1e9
    fish = []
    # q가 있는동안
    while q:
        # 선입 선출
        x, y, count = q.popleft()

        # 움직인 수가 플래그보다 크면 q 그만!
        if count > flag:
            break
        # 움직임 < 플래그라면 방향델타 순회
        for k in range(4):
            # 새 좌표 임시 저장
            nx, ny = x + dx[k], y + dy[k]
            # 범위 밖이면 안움직일거야
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            # 먹이가 아기상어보다 크거나 방문했다면 가지 않을거야
            if arr[nx][ny] > size or visited[nx][ny]:
                continue
            # 안에 먹이가 있고, 크기가 아기상어보다 작다면
            if arr[nx][ny] != 0 and arr[nx][ny] < size:
                # 먹을거야! 뇸
                fish.append((nx, ny, count + 1))
                flag = count

            # 방문 체크
            visited[nx][ny] = True
            # q에 넣기
            q.append((nx, ny, count + 1))
    # 먹은 물고기 수가 0보다 크면
    if len(fish) > 0:
        # 정렬하고 = 먹는 순서
        fish.sort()
        # 저장한거 꺼내서
        x, y, move = fish[0][0], fish[0][1], fish[0][2]
        move_num += move
        eat += 1
        arr[x][y] = 0
        if eat == size:
            size += 1
            eat = 0
        sx, sy = x, y
    else:
        break

print(move_num)