import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame
from copy import deepcopy

dr = [0, -1, -1, -1, 0, 1, 1, 1]
dc = [-1, -1, 0, 1, 1, 1, 0, -1]

# 상 좌 하 우
shark_dr = [-1, 0, 1, 0]
shark_dc = [0, -1, 0, 1]


# 2. 물고기 한 칸 이동
def fish_move():

    # 물고기가 해당 방향으로 이동할 수 있는지 확인하는 함수
    def fish_can_move(nr, nc):
        # 격자의 범위를 벗어나는 칸
        if not (0 <= nr < 4 and 0 <= nc < 4):
            return False

        # 상어가 있는 칸
        if nr == sr and nc == sc:
            return False

        # 물고기의 냄새가 있는 칸
        if fish_smell[nr][nc]:
            return False

        return True

    new_matrix = [[[] for _ in range(4)] for _ in range(4)]
    for r in range(4):
        for c in range(4):
            # 기존 matrix에 있는 물고기들 확인
            while matrix[r][c]:
                d = matrix[r][c].pop()
                for i in range(8):
                    # 방향 설정
                    nd = (d - i) % 8
                    nr = r + dr[nd]
                    nc = c + dc[nd]
                    # 해당 방향으로 이동할 수 있으면 새로운 matrix에 추가
                    if fish_can_move(nr, nc):
                        new_matrix[nr][nc].append(nd)
                        break
                # 이동할 수 없으면 이동하지 않는다.
                else:
                    new_matrix[r][c].append(d)

    return new_matrix


# 3. 상어 세 칸 이동
def shark_move(s):

    # i, j, k 방향으로 상어가 이동할 때 잡아먹는 물고기 수
    def shark_move_ijk(r, c, i, j, k):
        fish_cnt = len(matrix[r][c])
        matrix_check = [[0]*4 for _ in range(4)]

        for DIR in [i, j, k]:
            nr = r + shark_dr[DIR]
            nc = c + shark_dc[DIR]
            if 0 <= nr < 4 and 0 <= nc < 4:
                if matrix_check[nr][nc]:
                    pass
                else:
                    matrix_check[nr][nc] = 1
                    fish_cnt += len(matrix[nr][nc])
                    r, c = nr, nc
            # 하나라도 범위 바깥이면 out
            else:
                return -1

        return fish_cnt

    r, c = sr, sc
    result_fish_cnt = 0
    result_ijk = -1

    # 방향 지정 => i, j, k 중 방향 하나 픽스하기
    for i in range(4):
        for j in range(4):
            for k in range(4):
                fish_cnt = shark_move_ijk(r, c, i, j, k)
                if result_ijk == -1 and fish_cnt != -1:
                    result_ijk = (i, j, k)
                if result_fish_cnt < fish_cnt:
                    result_fish_cnt = fish_cnt
                    result_ijk = (i, j, k)

    # 픽스된 방향으로 물고기 없애기
    for DIR in result_ijk:
        nr = r + shark_dr[DIR]
        nc = c + shark_dc[DIR]
        if matrix[nr][nc]:
            matrix[nr][nc] = []
            fish_smell[nr][nc].append(s)
        r, c = nr, nc

    return r, c


# 4. 물고기 냄새 사라짐
def fish_smell_remove(s):
    for r in range(4):
        for c in range(4):
            left_smell = []
            while fish_smell[r][c]:
                tmp = fish_smell[r][c].pop()
                # s가 아닌 것들은 left_smell에 남기기
                if tmp != s:
                    left_smell.append(tmp)
            fish_smell[r][c] = left_smell


M, S = map(int, input().split())
matrix = [[[] for _ in range(4)] for _ in range(4)]
for _ in range(M):
    fr, fc, d = map(int, input().split())
    matrix[fr-1][fc-1].append(d-1)
sr, sc = map(int, input().split())
sr -= 1; sc -= 1
fish_smell = [[[] for _ in range(4)] for _ in range(4)]

while S:
    # 1. 복제 마법 시전
    replication_matrix = deepcopy(matrix)

    # 2. 물고기 이동
    matrix = fish_move()

    # 3. 상어 이동해서 위치 변경
    sr, sc = shark_move(S)

    # 4. 물고기 냄새 사라짐
    fish_smell_remove(S+2)

    # 5. 복제 마법 완료
    for r in range(4):
        for c in range(4):
            while replication_matrix[r][c]:
                tmp = replication_matrix[r][c].pop()
                matrix[r][c].append(tmp)
    S -= 1

# print(DataFrame(matrix))
result = 0
for r in range(4):
    for c in range(4):
        result += len(matrix[r][c])
print(result)
