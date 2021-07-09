import sys
sys.stdin = open('input.txt')
q = lambda: map(int, sys.stdin.readline().split())

R, C = q()
arr = [list(q()) for _ in range(R)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
wall = []

def getArea():
    safe = 0
    virus = []
    for i in range(R):
        for j in range(C):
            if arr[i][j] == 0:
                safe += 1
            if arr[i][j] == 2:
                virus.append((i, j))
    return safe, virus


def setWall():
    if len(wall) == 3:
        SpreadVirus(wall)
        return

    for i in range(R):
        for j in range(C):
            if arr[i][j] == 0 and (i, j) not in wall:
                wall.append((i, j))
                setWall()
                wall.pop()



def SpreadVirus(wall):
    global MIN

    for r, c in wall:
        arr[r][c] = 1

    visit = [[0] * R for _ in range(C)]

    que = list(virus)
    cnt = 0

    while que:
        r, c = que.pop(0)
        visit[r][c] = 1

        if cnt > MIN:
            break

        for k in range(4):  # 4방 이동
            nr, nc = r + dr[k], c + dc[k]

            if not (0 <= nr < R and 0 <= nc < C):
                continue

            if visit[nr][nc]:
                continue

            if arr[nr][nc] == 1:
                continue

            que.append((nr, nc))
            visit[nr][nc] = 1
            cnt += 1

    MIN = min(MIN, cnt)

    for r, c in wall:
        arr[r][c] = 0




safe, virus = getArea()
MIN = 987654321
setWall()
print(safe, safe - MIN - 3)