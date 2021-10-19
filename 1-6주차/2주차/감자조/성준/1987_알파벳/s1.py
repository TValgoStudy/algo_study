import sys
sys.stdin = open('input.txt')

def dfs(x, y, cnt):
    global result

    result = max(result, cnt)

    dy, dx = [1, -1, 0, 0], [0, 0, 1, -1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < R and 0 <= ny < C:
            if visited[strs[nx][ny]] == 0:
                visited[strs[nx][ny]] = 1
                dfs(nx, ny, cnt+1)
                visited[strs[nx][ny]] = 0

R, C = map(int, input().split())
strs = list(list(map(lambda x: ord(x) - 65, input())) for _ in range(R))

visited = [0] * 26
visited[strs[0][0]] = 1

result = 1
dfs(0, 0, 1)
print(result)