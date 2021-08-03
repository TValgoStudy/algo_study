import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame


# matrix 만들기
N = int(input())
matrix = [[0] * N for _ in range(N)]
matrix[0][0] = '.'

# matrix에 사과 배치하기
# 입력 기준이 0, 0 부터인지 1, 1 부터인지 확인
K = int(input())
for _ in range(K):
    r, c = map(int, input().split())
    matrix[r-1][c-1] = 1

# 뱀의 방향 정보
L = int(input())
goes = [input().split() for _ in range(L)]

# 상 우 하 좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# 왼쪽(C가 'L') 또는 오른쪽(C가 'D')
time, t, DIR, d = 0, 0, 'D', 1
snake = [(0, 0)]
r, c = 0, 0

while 1:
    # 현재 시간이 방향 회전할 시간이면 회전 아니면 그대로 (-1 % 4 = 3)
    if t < L and time == int(goes[t][0]):
        d = (d + 1) % 4 if goes[t][1] == 'D' else (d - 1) % 4
        t += 1

    # 다음 칸 확인해서 맵 밖이면 끝
    nr = r + dr[d]
    nc = c + dc[d]
    if not (0 <= nr < N and 0 <= nc < N):
        break

    # 다음 칸이 맵 안이면
    # 뱀 몸이면 끝
    if matrix[nr][nc] == '.':
        break
    # 사과면 이동하고 몸 길이 늘어남
    elif matrix[nr][nc] == 1:
        matrix[nr][nc] = '.'
        snake.append((nr, nc))
        r, c = nr, nc
    # 그냥 맵이면 꼬리는 삭제하고 이동
    else:
        tr, tc = snake.pop(0)
        matrix[tr][tc] = 0

        matrix[nr][nc] = '.'
        snake.append((nr, nc))
        r, c = nr, nc

    # 시간 +1 초
    time += 1

print(time+1)