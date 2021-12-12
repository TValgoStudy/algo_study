import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame

# 오른, 왼, 위, 아래
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]


# 1. 집에 있는 모든 온풍기에서 바람이 한 번 나옴
def hot_air_one(d, temp, temp_wind):
    if temp < 1:
        return

    next_temp_wind = set()
    while temp_wind:
        r, c = temp_wind.pop()

        nr = r + dr[d]
        nc = c + dc[d]

        # 다음거
        if 0 <= nr < R and 0 <= nc < C and wall_check(nr, nc, d):
            next_temp_wind.add((nr, nc))

        # 위, 아래 => 양쪽으로
        if d == 2 or d == 3:
            nc1 = c + dc[d] + 1
            nc2 = c + dc[d] - 1
            if 0 <= nr < R:
                if 0 <= nc1 < C and wall_check(nr, nc1, d) and wall_check(r, c, 0):
                    next_temp_wind.add((nr, nc1))
                if 0 <= nc2 < C and wall_check(nr, nc2, d) and wall_check(r, c, 1):
                    next_temp_wind.add((nr, nc2))
        # 왼, 오른 => 위아래
        else:
            nr1 = r + dr[d] + 1
            nr2 = r + dr[d] - 1
            if 0 <= nc < C:
                if 0 <= nr1 < R and wall_check(nr1, nc, d) and wall_check(r, c, 3):
                    next_temp_wind.add((nr1, nc))
                if 0 <= nr2 < R and wall_check(nr2, nc, d) and wall_check(r, c, 2):
                    next_temp_wind.add((nr2, nc))

    # 다음 온도 미리 작성
    for r, c in next_temp_wind:
        total_temp[r][c] += temp

    hot_air_one(d, temp-1, next_temp_wind)


def wall_check(r, c, d):
    # 오른
    if d == 0 and wall[r][c][1]:
        return False
    # 왼
    elif d == 1 and wall[r][c][0]:
        return False
    # 위
    elif d == 2 and wall[r][c][3]:
        return False
    # 아래
    elif d == 3 and wall[r][c][2]:
        return False
    return True


# 2. 온도가 조절됨
def temp_control():
    new_total_temp = [[0] * C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            new_total_temp[r][c] += total_temp[r][c]
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < R and 0 <= nc < C and total_temp[r][c] > total_temp[nr][nc] and wall_check(nr, nc, i):
                    temp_division = (total_temp[r][c] - total_temp[nr][nc]) // 4
                    new_total_temp[nr][nc] += temp_division
                    new_total_temp[r][c] -= temp_division
    return new_total_temp


# 3. 온도가 1 이상인 가장 바깥쪽 칸의 온도가 1씩 감소
def temp_decrease():
    for c in range(C):
        if total_temp[0][c]:
            total_temp[0][c] -= 1
        if total_temp[R-1][c]:
            total_temp[R-1][c] -= 1
    if R > 2:
        for r in range(1, R-1):
            if total_temp[r][0]:
                total_temp[r][0] -= 1
            if total_temp[r][C-1]:
                total_temp[r][C-1] -= 1


# 5. 조사하는 모든 칸의 온도가 K 이상이 되었는지 검사
def temp_ok_check():
    for r, c in temp_ok_list:
        if total_temp[r][c] < K:
            return False
    return True



R, C, K = map(int, input().split())

# 온풍기 위치, 방향
hot_air = []
temp_ok_list = []
matrix = [list(map(int, input().split())) for _ in range(R)]
for r in range(R):
    for c in range(C):
        if matrix[r][c] == 5:
            temp_ok_list.append((r, c))
        elif matrix[r][c]:
            hot_air.append((r, c, matrix[r][c]-1))

# 벽 위치, 방향
# wall = {}
# for _ in range(int(input())):
#     r, c, d = map(int, input().split())
#     wall[(r-1, c-1, d)] = 1

# 오른, 왼, 위, 아래
wall = [[[0, 0, 0, 0] for _ in range(C)] for _ in range(R)]
for _ in range(int(input())):
    r, c, d = map(int, input().split())
    r -= 1
    c -= 1
    if d == 0:
        wall[r][c][2] = 1
        wall[r][c-1][3] = 1
    else:
        wall[r][c][0] = 1
        wall[r][c+1][1] = 1



# 온도
total_temp = [[0]*C for _ in range(R)]

choco = 0
while choco < 101:
    # 1. 집에 있는 모든 온풍기에서 바람이 한 번 나옴
    for r, c, d in hot_air:
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < R and 0 <= nc < C:
            total_temp[nr][nc] += 5
            hot_air_one(d, 4, {(nr, nc)})
        print(DataFrame(total_temp))
        print()
    # 2. 온도가 조절됨
    total_temp = temp_control()

    # 3. 온도가 1 이상인 가장 바깥쪽 칸의 온도가 1씩 감소
    temp_decrease()

    # 4. 초콜릿을 하나 먹는다.
    choco += 1

    # 5. 조사하는 모든 칸의 온도가 K 이상이 되었는지 검사
    if temp_ok_check():
        break



print(choco)

# 집에 있는 모든 온풍기에서 바람이 한 번 나옴
# 온도가 조절됨
# 온도가 1 이상인 가장 바깥쪽 칸의 온도가 1씩 감소
# 초콜릿을 하나 먹는다.
# 조사하는 모든 칸의 온도가 K 이상이 되었는지 검사. 모든 칸의 온도가 K이상이면 테스트를 중단하고, 아니면 1부터 다시 시작한다.
