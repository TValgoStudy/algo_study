import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame

# 오른쪽 왼쪽 위 아래
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]


def go_stay(num):
    r, c, d = chesses[num]
    # num 번 체스의 인덱스 찾기
    idx = chess_map[r][c].index(num)
    # 해당 인덱스 이후로 함께 이동하고 나머지는 그자리에
    go = chess_map[r][c][idx:]
    stay = chess_map[r][c][:idx]
    return go, stay


def func(num):
    r, c, d = chesses[num]
    nr, nc = r + dr[d], c + dc[d]

    # 체스판을 벗어나거나, 파란색이면 => 방향 바꿔서 nr, nc 갱신
    if not (0 <= nr < N and 0 <= nc < N) or color_map[nr][nc] == 2:
        # 말의 이동 방향을 바꾼다 & chesses 체스 정보 리스트에서 방향 갱신
        if d == 0: nd = 1
        elif d == 1: nd = 0
        elif d == 2: nd = 3
        else: nd = 2
        chesses[num][2] = nd
        nr, nc = r + dr[nd], c + dc[nd]

    # 두번째로 체스판을 벗어나거나, 파란색이면 => 가만히 있기
    if not (0 <= nr < N and 0 <= nc < N) or color_map[nr][nc] == 2:
        return

    # num 번째 수를 이동할 예정. 같이 이동하는게 go, 남는게 stay
    go, stay = go_stay(num)

    # 현재 위치에는 이동 안하는 나머지(stay)들을 써주고,
    chess_map[r][c] = stay

    # 다음 위치에는 이동하는 것들(go)을 추가해준다.
    # 흰색 => 그대로, 빨간색 => 역순
    if color_map[nr][nc] == 0:
        chess_map[nr][nc].extend(go)
    elif color_map[nr][nc] == 1:
        chess_map[nr][nc].extend(go[::-1])

    # stay, go 체스 정보 리스트에서 좌표 갱신
    for n in stay:
        chesses[n][0], chesses[n][1] = r, c
    for n in go:
        chesses[n][0], chesses[n][1] = nr, nc


N, K = map(int, input().split())
color_map = [list(map(int, input().split())) for _ in range(N)]
chess_map = [[[] for _ in range(N)] for _ in range(N)]

chesses = []
for k in range(K):
    r, c, d = map(int, input().split())
    r, c, d = r-1, c-1, d-1
    # chesses 리스트에 k번째 체스 정보 추가
    chesses.append([r, c, d])
    # chess_map 좌표에 k번째 체스 추가
    chess_map[r][c].append(k)

turn, small_turn, flag = 0, -1, 1
while turn <= 1000 and flag:
    # small_turn은 0 부터 시작, turn은 1부터 시작
    # small_turn이 0이 될 때마다(=사이클 시작할 때마다) turn +1
    small_turn = (small_turn + 1) % K
    if small_turn == 0:
        turn += 1

    # small_turn올라가면 해당 값을 인덱스로 func돌리기
    func(small_turn)

    # chess_map에서 체스 4개 이상이면 그만두기
    for r in range(N):
        for c in range(N):
            if len(chess_map[r][c]) >= 4:
                flag = 0

if turn > 1000:
    print(-1)
else:
    print(turn)
