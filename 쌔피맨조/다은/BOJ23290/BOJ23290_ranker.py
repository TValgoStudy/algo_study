# 마법사 상어와 복제

# 1. 복제
# 2. 물고기 이동 1칸 / 상어, 냄새, 범위밖으로 이동불가 / 이동가능할때까지 반시계 45도 회전, 그래도 없으면 이동x
# 3. 상어이동 3칸 / 가장 많이 물고기를 먹는 경로로 / 같은 경우 사전순 / 물고기는 먹힐때 냄새를 남김
# 4. 2턴전의 물고기 냄새가 사라짐
# 5. 복제완료, 복제했던 물고기들 반영

#  1부터 순서대로 ←, ↖, ↑, ↗, →, ↘, ↓, ↙

# 물고기 이동방향, 8방향
dr = [1, 0, -1, -1, -1, 0, 1, 1]
dc = [-1, -1, -1, 0, 1, 1, 1, 0]  # 8, 1 ~ 7

# 상어이동 방향, 상좌하우
drc_shark = [(-1, 0), (0, -1), (1, 0), (0, 1)]

M, S = map(int, input().split())

fish_dict = {}
fish_smell_board = [[0] * 5 for _ in range(5)]
for _ in range(M):
    fx, fy, d = map(int, input().split())
    try:
        fish_dict[(fx, fy, d % 8)] += 1
    except:
        fish_dict[(fx, fy, d % 8)] = 1

# 상어위치
sx, sy = map(int, input().split())

for _ in range(S):  # S번 반복

    # 1. 복제
    next_fish_dict = {}

    # 2. 물고기 이동
    for (fx, fy, d), cnt in fish_dict.items():
        for i in range(8):
            nr = fx + dr[(d - i) % 8]
            nc = fy + dc[(d - i) % 8]
            if 0 < nr < 5 and 0 < nc < 5 and not fish_smell_board[nr][nc] and (nr, nc) != (sx, sy):
                try:
                    next_fish_dict[(nr, nc, (d - i) % 8)] += cnt
                except:
                    next_fish_dict[(nr, nc, (d - i) % 8)] = cnt
                break

        else:  # 이동을 못할 때
            try:
                next_fish_dict[(fx, fy, d)] += cnt
            except:
                next_fish_dict[(fx, fy, d)] = cnt

    fish_cnt_board = [[0] * 5 for _ in range(5)]
    for (fx, fy, d), cnt in next_fish_dict.items():
        fish_cnt_board[fx][fy] += cnt

    # 3. 상어이동(3칸)
    max_eat_cnt = -1
    eat_fish_rc = []
    for i in range(4):
        nr1 = sx + drc_shark[i][0]
        nc1 = sy + drc_shark[i][1]
        if not (0 < nr1 < 5 and 0 < nc1 < 5):
            continue

        for j in range(4):
            nr2 = nr1 + drc_shark[j][0]
            nc2 = nc1 + drc_shark[j][1]
            if not (0 < nr2 < 5 and 0 < nc2 < 5):
                continue

            for k in range(4):
                nr3 = nr2 + drc_shark[k][0]
                nc3 = nc2 + drc_shark[k][1]
                if not (0 < nr3 < 5 and 0 < nc3 < 5):
                    continue

                if (nr1, nc1) == (nr3, nc3):
                    if max_eat_cnt < fish_cnt_board[nr1][nc1] + fish_cnt_board[nr2][nc2]:
                        max_eat_cnt = fish_cnt_board[nr1][nc1] + fish_cnt_board[nr2][nc2]
                        eat_fish_rc = [(nr1, nc1), (nr2, nc2), (nr3, nc3)]

                else:
                    if max_eat_cnt < fish_cnt_board[nr1][nc1] + fish_cnt_board[nr2][nc2] + fish_cnt_board[nr3][nc3]:
                        max_eat_cnt = fish_cnt_board[nr1][nc1] + fish_cnt_board[nr2][nc2] + fish_cnt_board[nr3][nc3]
                        eat_fish_rc = [(nr1, nc1), (nr2, nc2), (nr3, nc3)]

    # 상어가 잡아먹어야 하는 칸들
    for r, c in eat_fish_rc:
        for i in range(8):
            try:
                del next_fish_dict[(r, c, i)]
                fish_smell_board[r][c] = 3
            except:
                continue

    # 상어의 다음 위치
    sx, sy = eat_fish_rc[-1]

    # 4. 냄새 제거
    for r in range(1, 5):
        for c in range(1, 5):
            if fish_smell_board[r][c]:
                fish_smell_board[r][c] -= 1

    # 5. 복제완료
    for (fx, fy, d), cnt in fish_dict.items():
        try:
            next_fish_dict[(fx, fy, d)] += cnt
        except:
            next_fish_dict[(fx, fy, d)] = cnt

    fish_dict = next_fish_dict

print(sum(fish_dict.values()))