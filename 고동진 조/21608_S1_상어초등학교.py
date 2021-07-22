import sys
sys.stdin = open('input.txt', 'r')

# 번호는 1번부터 N^2
# 가장 좋아하는 학생이 인접한 칸에 가장 많은 칸으로
# 여러개라면 비어있는 칸이 가장 많은 자리.
# 또 겹친다면 행의 번호가 가장 작고, 열의 번호가 가장 작은 칸

input = sys.stdin.readline


def inrange(r: int, c: int) -> bool:
    return 0 <= r < N and 0 <= c < N


N = int(input())
answer = 0
board = [[0 for _ in range(N)] for _ in range(N)]
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
infos = [list(map(int, input().split())) for _ in range(N**2)]
for info_origin in infos:
    info = info_origin[:]
    me = info.pop(0)
    possible = [] # 0번 : 친구, 1번 : 빈칸, 2번 : 위치

    for r in range(N):
        for c in range(N):
            if board[r][c]: continue
            idx = N * r + c
            temp = [0, 0, idx]
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if not inrange(nr, nc): continue
                if board[nr][nc] in info:
                    temp[0] += 1
                elif board[nr][nc] == 0:
                    temp[1] += 1

            possible.append(temp)

    possible.sort(key=lambda x: [x[0], x[1], -x[2]])
    pos_r = possible[-1][2] // N
    pos_c = possible[-1][2] % N
    board[pos_r][pos_c] = me


infos.sort()
for r in range(N):
    for c in range(N):
        cnt = 0
        for i in range(4):
            nr = dr[i] + r
            nc = dc[i] + c
            if not inrange(nr, nc): continue
            if board[nr][nc] in infos[board[r][c] - 1][1:]:
                cnt += 1

        if cnt:
            answer += 10 ** (cnt - 1)

print(answer)
