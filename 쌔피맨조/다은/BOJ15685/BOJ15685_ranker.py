a = [[0]*101 for _ in range(101)]
dr = [[0]]

for _ in range(10):
    dr.append(dr[-1] + [i+1 for i in dr[-1][::-1]])

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for _ in range(int(input())):
    x, y, d, g = map(int, input().split())
    a[x][y] = 1
    for k in dr[g]:
        x += dx[(d + k) % 4]
        y += dy[(d + k) % 4]
        a[x][y] = 1

cnt = 0
for i in range(100):
    for j in range(100):
        if a[i][j] and a[i][j+1] and a[i+1][j] and a[i+1][j+1]:
            cnt += 1

print(cnt)

