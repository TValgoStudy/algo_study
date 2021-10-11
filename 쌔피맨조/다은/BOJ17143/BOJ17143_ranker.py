import sys
sys.stdin = open("input.txt", "r")

def solve(sea):
    new_sea = [[0] * (C + 1) for _ in range(R + 1)]
    for r in range(1, R + 1):
        for c in range(1, C + 1):
            # 상어가 없으면 패스
            if not sea[r][c]:
                continue

            # 상어가 있으면 진행
            s, d, z = sea[r][c]
            nr, nc = r + s * dir[d][0], c + s * dir[d][1]

            # 범위 바깥이면
            while nr < 1 or nr > R:
                # nr이 1 보다 작으면 방향은 아래
                if nr < 1:
                    d = 2
                    nr = 2 - nr
                # nr이 R보다 크면 방향은 위
                elif nr > R:
                    d = 1
                    nr = R + R - nr

            # 범위 바깥이면
            while nc < 1 or nc > C:
                # nc가 1보다 작으면 방향은 오른쪽
                if nc < 1:
                    d = 3
                    nc = 2 - nc
                # nc가 C보다 크면 방향은 왼쪽
                elif nc > C:
                    d = 4
                    nc = C + C - nc

            # 새로운 값으로 갱신
            if new_sea[nr][nc] != 0:
                if z > new_sea[nr][nc][2]:
                    new_sea[nr][nc] = [s, d, z]
            else:
                new_sea[nr][nc] = [s, d, z]
    return new_sea


R, C, m = map(int, input().split())
sea = [[0] * (C + 1) for i in range(R + 1)]
dir = [[0, 0], [-1, 0], [1, 0], [0, 1], [0, -1]]

for k in range(m):
    i, j, s, d, z = map(int, input().split())
    # 한 왕복거리 내로 s 값 조절
    s %= ((R if d <= 2 else C) - 1) * 2
    sea[i][j] = [s, d, z]

cur = 0
result = 0
while cur < C:
    cur += 1
    # 2. 해당 열에서 땅과 제일 가까운 상어를 잡는다.
    for k in range(1, R + 1):
        if sea[k][cur] != 0:
            result += sea[k][cur][2]
            sea[k][cur] = 0
            break
    # 3. 상어가 이동한다.
    sea = solve(sea)

print(result)