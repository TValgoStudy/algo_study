# 상어가 먹을 수 있는 물고기 번호의 합의 최댓값을 구해보자.
# 북동, 북, 북서, 서, 남서, 남, 남동, 동
dr = [-1, -1, -1, 0, 1, 1, 1, 0]
dc = [1, 0, -1, -1, -1, 0, 1, 1]

live_fishes = [1] * 17
fishes_position = [(-1, -1)] * 17

# 첫째 줄부터 4개의 줄에 각 칸의 들어있는 물고기의 정보가 1번 행부터 순서대로 주어진다.
# 물고기의 정보는 두 정수 ai, bi로 이루어져 있고, ai는 물고기의 번호, bi는 방향을 의미한다.
#  방향 bi는 8보다 작거나 같은 자연수를 의미하고, 1부터 순서대로 ↑, ↖, ←, ↙, ↓, ↘, →, ↗ 를 의미한다.
aquarium = []
# 물고기 번호의 합의 최댓값 == sum(ai_eaten)
ans = 0
for _ in range(4):
    tmp = list(map(int, input().split()))
    for i in range(4):
        if tmp[2 * i + 1] == 8:
            tmp[2 * i + 1] = 0
    # (ai, bi)
    tmp2 = [(tmp[2 * i], tmp[2 * i + 1]) for i in range(4)]
    aquarium.append(tmp2)
# 물고기 위치 미리 찾아놓자.
for row in range(4):
    for col in range(4):
        fishes_position[aquarium[row][col][0]] = (row, col)


def dfs(moved_aquarium, new_fishes_position, new_live_fishes, new_shark=(0, 0), eaten_fishes=0):
    global ans
    # 상어 먹을 차례 시작은 (0, 0)
    # 움직인 곳의 물고기 먹기
    shark_row, shark_col = new_shark
    ai, shark_direction = moved_aquarium[shark_row][shark_col]
    eaten_fishes += ai
    new_live_fishes[moved_aquarium[shark_row][shark_col][0]] = 0
    moved_aquarium[shark_row][shark_col] = (0, 0)
    if eaten_fishes > ans:
        ans = eaten_fishes

    # 물고기 차례
    for idx in range(1, 17):
        if not new_live_fishes[idx]:
            continue
        row, col = new_fishes_position[idx]
        ai, bi = moved_aquarium[row][col]
        for add in range(8):
            d = (bi + add) % 8
            nr = row + dr[d]
            nc = col + dc[d]
            if nr < 0 or nr >= 4 or nc < 0 or nc >= 4 or (nr, nc) == new_shark:
                continue
            # 방향 정해지면 방향 실제 변화
            moved_aquarium[row][col] = (ai, d)
            # 이동하는 칸과 교환 후 이동 그만
            new_fishes_position[idx] = (nr, nc)
            new_fishes_position[moved_aquarium[nr][nc][0]] = (row, col)
            moved_aquarium[row][col], moved_aquarium[nr][nc] = moved_aquarium[nr][nc], moved_aquarium[row][col]
            break

    # 상어가 움직일 차례

    for multiple in range(1, 4):
        nr = shark_row + dr[shark_direction]*multiple
        nc = shark_col + dc[shark_direction]*multiple
        if nr < 0 or nr >= 4 or nc < 0 or nc >= 4 or moved_aquarium[nr][nc][0] == 0:
            continue

        # deep copy
        duplicated_aquarium = []
        for i in range(4):
            duplicated_aquarium.append(moved_aquarium[i][:])

        # 1차원 리스트 원소가 tuple 이기에 1차원도 deepcopy가 된다.
        # position이 (row, col)은 mutable이여서 deepcopy로 동작 [row, col] 이면 for statement로 복사해야 된다.
        duplicated_fishes_position = new_fishes_position[:]
        duplicated_live_fishes = new_live_fishes[:]

        dfs(duplicated_aquarium, duplicated_fishes_position, duplicated_live_fishes, new_shark=(nr, nc), eaten_fishes=eaten_fishes)
    return


dfs(aquarium, fishes_position, live_fishes)
print(ans)
