import sys
sys.stdin = open("input6.txt", "r")

x = lambda: map(int, input().split())
N, M = x()
a, b, c = x()
m = []
d = [-1, 0, 1, 0, -1, 0, 1, 0]
cnt = 0

for _ in range(N):
    m.append(list(x()))

ck = 0
while m[a][b] != 1:
    # 해당 위치 청소
    if m[a][b] == 0:
        cnt += 1
    m[a][b] = -1
    ck = 1
    # 해당 위치에서 4방향 탐색
    for i in range(1, 5):
        x = a + d[c - i]
        y = b + d[3 - c + i]
        # 청소할 수 있는 곳이면 ck = 0
        if m[x][y] == 0:
            a = x
            b = y
            c = (c - i) % 4
            ck = 0
            break
    # 4방향 탐색으로 청소 못하면 ck=1
    # 뒤로 이동해서 그곳이 1이면 while 종료
    if ck:
        a += d[c + 2]
        b += d[c + 3]

print(cnt)