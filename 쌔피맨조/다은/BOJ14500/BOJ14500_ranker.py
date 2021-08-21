import sys
N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]

def DFS(depth, y, x, sumval):
    global result

    if sumval + (3 - depth) * maxval <= result:
        return

    if depth == 3:
        result = max(result, sumval)
        return

    else:
        for i in range(4):
            dy, dx = y + dir[i][0], x + dir[i][1]
            if 0 > dy or N <= dy or 0 > dx or M <= dx or history[dy][dx]:
                continue
            if depth == 1:
                history[dy][dx] = True
                DFS(depth + 1, y, x, sumval + arr[dy][dx])
                history[dy][dx] = False
            history[dy][dx] = True
            DFS(depth + 1, dy, dx, sumval + arr[dy][dx])
            history[dy][dx] = False

result = 0
maxval = max(map(max, arr))
history = [[False] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        history[i][j] = True
        DFS(0, i, j, arr[i][j])
        history[i][j] = False
print(result)