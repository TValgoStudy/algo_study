import sys
from pandas import DataFrame
sys.stdin = open("input.txt", "r")


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(s, e):
    global dist

    visited = [[0] * N for _ in range(N)]
    visited[s[0]][s[1]] = 1
    result = 999999

    q = [s]
    while q:
        r, c = q.pop(0)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            # 범위 내 & 아직 방문 안한 곳 & 상어 크기보다 작거나 같은 물고기자리만 지나가기 & 상어자리는 패스
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and (IN[nr][nc] <= baby_shark or IN[nr][nc] == 9):
                q.append((nr, nc))
                visited[nr][nc] = visited[r][c] + 1
        if visited[e[0]][e[1]]:
            result = visited[e[0]][e[1]] - 1
            if dist > result:
                dist = result
            break

    return result


N = int(input())
IN = [list(map(int, input().split())) for _ in range(N)]

fishes_position = []
for r in range(N):
    for c in range(N):
        # 아기 상어 위치
        if IN[r][c] == 9:
            br, bc = (r, c)
        # 모든 물고기 위치
        elif IN[r][c]:
            fishes_position.append((r, c))

# 크기 2짜리 아기상어가 먹을 수 있는 물고기 can_eat
can_eat = [(r, c) for r, c in fishes_position if 0 < IN[r][c] < 2]
# 상어 크기 baby_shark, 시간 time, 먹은 물고기 수 eat_num
baby_shark = 2
time, eat_num = 0, 0

# 먹을 수 있는 물고기가 있으면 반복
while can_eat:
    dist = 999999
    # 거리, 행, 열 기준으로 오름차순 정렬
    can_eat.sort(key=lambda x: (bfs((br, bc), x), x[0], x[1]))
    # 아기상어 위치 변경 & 해당 공간 값 0으로 변경
    br, bc = can_eat.pop(0)
    IN[br][bc] = 0
    # 이동 시간 추가 & 먹은 물고기수 추가
    if dist == 999999:
        break
    time += dist
    eat_num += 1

    # 먹은 수가 크기랑 같아지면 +1, 먹을 수 있는 물고기 재설정
    if eat_num == baby_shark:
        eat_num = 0
        baby_shark += 1
        can_eat = [(r, c) for r, c in fishes_position if 0 < IN[r][c] < baby_shark]

print(time)

