#드래곤 커브
#1시작 점, 2시작 방향, 3세대
from sys import*

input = stdin.readline

v = [0]
ans = 0
MAX = 101
a = [[0]*MAX for _ in range(MAX)]
dd = [(1, 0), (0, -1), (-1, 0), (0, 1)]

# 비트연산으로 1,2,4,8, ...(세대 개수=k)
for i in range(1, 11):
    k = 1 << (i-1)
    for j in range(k):
        # 뒤로 훑으면서 (+1) % 4 = (방향 90도) 돌려서 저장
        v.append((v[k-j-1]+1) % 4)

for _ in range(int(input())):
    x, y, d, g = map(int, input().split())
    a[x][y] = 1
    # 세대 수 만큼
    for i in range(1 << g):
        # 주어진 방향에 90도로 꺾어가며 체크
        dx, dy = dd[(v[i] + d) % 4]
        x, y = x + dx, y + dy
        a[x][y] = 1

# 맵 탐색하며 사각형이면 +1
for i in range(100):
    for j in range(100):
        if a[i][j] and a[i+1][j] and a[i][j+1] and a[i+1][j+1]:
            ans += 1

print(ans)
