import sys
from pandas import DataFrame
sys.stdin = open("input.txt", "r")

# 1시간 15분

dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

N = int(input())
matrix = [[0]*101 for _ in range(101)]

for _ in range(N):
    x, y, d, g = map(int, input().split())
    # 초기 0세대 드래곤 커브
    curve = 0
    current = [(x, y), (x + dx[d], y + dy[d])]

    while curve != g:
        next = []
        # 가장 마지막에 추가된 지점이 회전 중심
        x0, y0 = current[-1]

        # 지금까지 쌓아온 것을 뒤로 돌아가며 회전시킨다
        for x, y in current[:-1][::-1]:
            nx = x0 + y0 - y
            ny = -x0 + y0 + x
            next.append((nx, ny))

        # 커브 +1 하고 current에 회전시킨 것들 붙여줌
        curve += 1
        current += next

    # 드래곤 커브들의 위치 1로 다 바꿔줌
    for x, y in current:
        matrix[y][x] = 1

# 4 꼭짓점 모두 1이면 result +1
result = 0
for y in range(100):
    for x in range(100):
        if matrix[x][y] and matrix[x+1][y] and matrix[x][y+1] and matrix[x+1][y+1]:
            result += 1

print(result)
