import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame

# 위, 아래, 왼, 오른
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def func():
    for idx, shark_pos in enumerate(sharks_pos):
        if idx == 0: continue
        r, c = shark_pos
        d = sharks_dir[idx]

        # 상어가 이미 죽었으면 패스
        if r == -1:
            sharks_move[idx].append((-1, -1))
            if sharks_move[idx][0] == -1:
                continue
            if len(sharks_move[idx]) > k:
                r, c = sharks_move[idx].pop(0)
                if r != -1:
                    matrix_check[r][c] = 0
            continue

        # idx 번째 상어 다음 방향 결정하기
        if d == 0: next_d = 1
        elif d == 1: next_d = 0
        elif d == 2: next_d = 3
        elif d == 3: next_d = 2

        # idx 번째 상어의 현재 방향의 우선순위 순서대로 nr, nc 구하기
        for i in sharks_priority[idx][d]:
            nr = r + dr[i]
            nc = c + dc[i]
            # 이동할 수 있으면 해당 방향으로 결정
            if 0 <= nr < N and 0 <= nc < N and not matrix_check[nr][nc]:
                next_d = i
                break

        # 이동하고 체크
        nr = r + dr[next_d]
        nc = c + dc[next_d]

        # 더 큰 상어가 미리 자리에 있으면 잡아먹힌다
        if matrix_check[nr][nc] and matrix_check[nr][nc] < idx:
            sharks_pos[idx] = (-1, -1)
            sharks_move[idx].append((-1, -1))

        # 아니면 해당 자리 차지
        else:
            sharks_pos[idx] = (nr, nc)
            matrix_check[nr][nc] = idx
            sharks_move[idx].append((nr, nc))

        # k보다 길어지면 앞에 있는 것 삭제
        if len(sharks_move[idx]) > k:
            r, c = sharks_move[idx].pop(0)
            if r != -1:
                matrix_check[r][c] = 0



N, M, k = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
# 상어 현재 방향 (인덱스 1~M 사용)
sharks_dir = [0] + list(map(int, input().split()))
# 우선 순위 (인덱스 1~M 사용)
sharks_priority = [0] + [[list(map(int, input().split())) for _ in range(4)] for _ in range(M)]

for i in range(1, M+1):
    sharks_dir[i] -= 1

for x in range(1, M+1):
    for y in range(4):
        for z in range(4):
            sharks_priority[x][y][z] -= 1

# 냄새 있는 칸 체크
matrix_check = [[0]*N for _ in range(N)]
# 상어 이동 좌표 (인덱스 1~M 사용)
sharks_move = [[] for _ in range(M+1)]
# 상어 현재 좌표 (인덱스 1~M 사용)
sharks_pos = [0] * (M+1)
for r in range(N):
    for c in range(N):
        # matrix[r][c] 번 째 상어의 위치 & 이동 좌표 설정
        if matrix[r][c]:
            sharks_pos[matrix[r][c]] = (r, c)
            sharks_move[matrix[r][c]].append((r, c))
            matrix_check[r][c] = matrix[r][c]

time = 0
while 1:
    func()
    time += 1
    print(DataFrame(matrix_check))

    # 상어가 다 쫓겨났는지 세기
    tmp = 0
    for i in range(2, M+1):
        if sharks_pos[i][0] < 0:
            tmp += 1
    if tmp == M-1:
        break


print(time)

