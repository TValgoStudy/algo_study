# 상어가 먹을 수 있는 물고기 번호의 합의 최댓값을 구해보자.
# 북동, 북, 북서, 서, 남서, 남, 남동, 동
dr = [-1, -1, -1, 0, 1, 1, 1, 0]
dc = [1, 0, -1, -1, -1, 0, 1, 1]

live_fishes = [1]*17
fishes_position = [(-1, -1)]*17

# 첫째 줄부터 4개의 줄에 각 칸의 들어있는 물고기의 정보가 1번 행부터 순서대로 주어진다.
# 물고기의 정보는 두 정수 ai, bi로 이루어져 있고, ai는 물고기의 번호, bi는 방향을 의미한다.
#  방향 bi는 8보다 작거나 같은 자연수를 의미하고, 1부터 순서대로 ↑, ↖, ←, ↙, ↓, ↘, →, ↗ 를 의미한다.
aquarium = []
# 물고기 번호의 합의 최댓값 == sum(ai_eaten)
ans = 0
for _ in range(4):
    tmp = list(map(int, input().split()))
    for i in range(4):
        if tmp[2*i+1] == 8:
            tmp[2*i+1] = 0
    # (ai, bi)
    tmp2 = [(tmp[2*i], tmp[2*i+1]) for i in range(4)]
    aquarium.append(tmp2)
# 물고기 위치 미리 찾아놓자.
for row in range(4):
    for col in range(4):
        fishes_position[aquarium[row][col][0]] = (row, col)




# 청소년 상어는 (0, 0)에 있는 물고기를 먹고, (0, 0)에 들어가게 된다.
shark = aquarium[0][0]
ans += shark[0]
live_fishes[shark[0]] = 0
# fishes_position[shark[0]] = (-1, -1)  # 굳이 넣을 필요는 없음
aquarium[0][0] = (0, 0)
shark_position = (0, 0)
# 상어의 방향은 (0, 0)에 있던 물고기의 방향과 같다. 이후 물고기가 이동한다.
while shark[0]:
    # 물고기는 번호가 작은 물고기부터 순서대로 이동한다.
    for idx in range(1, 17):
        if not live_fishes[idx]: # 안으로 안들어가도록 짠다.
            continue
        # 매번 찾지 말자
        # for row in range(4):
        #     for col in range(4):
        #         pass
        row, col = fishes_position[idx]
        ai, bi = aquarium[row][col]
        for add in range(8):
            d = (bi + add) % 8
            nr = row + dr[d]
            nc = col + dc[d]
            if nr < 0 or nr >= 4 or nc < 0 or nc >= 4 or (nr, nc) == shark_position:
                continue
            # 이동하는 칸과 교환후 이동 그만
            fishes_position[aquarium[nr][nc][0]] = (row, col)
            fishes_position[idx] = (nr, nc)
            # 실제 이동
            aquarium[row][col] = (ai, d)
            tmp = aquarium[nr][nc]
            aquarium[nr][nc] = aquarium[row][col]
            aquarium[row][col] = tmp
            break
    # 다시 상어 이동
    row, col = shark_position
    ai, bi = shark
    for multiple in range(3):
        nr = row + dr[bi] * multiple
        nc = col + dc[bi] * multiple
        if nr < 0 or nr >= 4 or nc < 0 or nc >= 4 or aquarium[nr][nc][0] == 0:
            continue
        new_aquarium = []
        for row in range(4):
            new_aquarium.append(aquarium[row][:])


        # 물고기 찾으면 잡아먹으러 간다.
        shark_position = (nr, nc)
        shark = aquarium[nr][nc]
        aquarium[nr][nc] = (0, 0)

        ans += shark[0]
        live_fishes[shark[0]] = 0
        fishes_position[shark[0]] = (-1, -1)  # 굳이 넣을 필요는 없음

    if ai == shark[0]:
        break
print(ans)
