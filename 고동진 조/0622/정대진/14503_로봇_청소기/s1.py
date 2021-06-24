N, M = map(int, input().split())
# d가 0인 경우에는 북쪽을, 1인 경우에는 동쪽을, 2인 경우에는 남쪽을, 3인 경우에는 서쪽
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
r, c, d = map(int, input().split())
# 빈 칸은 0, 벽은 1
matrix = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
# 1.현재 위치를 청소한다. 로봇 청소기가 있는 칸의 상태는 항상 빈 칸이다
while True:
    # 로봇 청소기는 이미 청소되어있는 칸을 또 청소하지 않으며
    if matrix[r][c] == 0:
        matrix[r][c] = 2
        cnt += 1
    # 2. 현재 위치에서 현재 방향을 기준으로 왼쪽방향부터 차례대로 탐색을 진행한다
    for _ in range(4):
        d -= 1
        if d < 0:
            d = 3
        # 2.1 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
        # 2.2 왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고 2번으로 돌아간다.
        nr = r + dr[d]
        nc = c + dc[d]
        if matrix[nr][nc] == 0:
            r = nr
            c = nc
            break
    # 3. 네 방향 모두 청소가 이미 되어있거나 벽
    else:
        # 3. 한칸 뒤쪽 확인
        nd = d - 2
        if nd < 0:
            nd += 4
        nr = r + dr[nd]
        nc = c + dc[nd]
        if matrix[nr][nc] == 1:
            break
        # matrix[nr][nc] == 2:
        else:
            r = nr
            c = nc

print(cnt)
