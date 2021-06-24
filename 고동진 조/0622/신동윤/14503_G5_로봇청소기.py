def inrange(row: int, col: int) -> bool:
    return 0 <= row < N and 0 <= col < M


N, M = map(int, input().split())
r, c, head = list(map(int, input().split()))
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]

# 0  1  2  3
# 북 동 남 서
# 왼쪽부터 탐색
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
answer = 0

while True:
    if answer > 100:
        debug = True

    if not visited[r][c]:
        answer += 1
        visited[r][c] = 1

    flag = 0
    for i in range(1, 5):
        nhead = head - i if head - i >= 0 else head - i + 4
        nr = r + dr[nhead]
        nc = c + dc[nhead]
        if inrange(nr, nc) and not visited[nr][nc] and board[nr][nc] == 0:
            r = nr
            c = nc
            head = nhead
            flag = 1
            break

    if flag == 0:
        nr = r - dr[head]
        nc = c - dc[head]
        if inrange(nr, nc) and board[nr][nc] == 0:
            r, c = nr, nc
        elif not inrange(nr, nc):
            break
        elif inrange(nr, nc) and board[nr][nc] == 1:
            break

print(answer)



