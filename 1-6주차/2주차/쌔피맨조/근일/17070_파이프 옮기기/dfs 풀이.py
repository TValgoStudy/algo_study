import sys
# input = sys.stdin.readline

sys.stdin = open('input.txt')

def move_the_pipe(r, c, pipe_status):

    global cnt

    if r == N and c == N:
        if room[N][N] == 2:
            cnt += 1
        return

    if room[N][N] == 1:
        return

    else:
        # pipe_status가 가로
        if pipe_status == 1:

            # 이동할 수 없으면
            if room[r][c + 1] != 0 and room[r + 1][c + 1] != 0 and room[r + 1][c] != 0:
                return

            else:
                # 만약에 가로로 이동 가능하면
                if room[r][c + 1] == 0:
                    room[r][c + 1] = 2
                    move_the_pipe(r, c + 1, 1)
                    room[r][c + 1] = 0

                # 만약에 대각으로 이동 가능하면
                if room[r][c + 1] == 0 and room[r + 1][c + 1] == 0 and room[r + 1][c] == 0:
                    room[r][c + 1], room[r + 1][c + 1], room[r + 1][c] = 2, 2, 2
                    move_the_pipe(r + 1, c + 1, 3)
                    room[r][c + 1], room[r + 1][c + 1], room[r + 1][c] = 0, 0, 0

        # pipe_status가 세로
        elif pipe_status == 2:

            if room[r][c + 1] != 0 and room[r + 1][c + 1] != 0 and room[r + 1][c] != 0:
                return

            else:
                # 만약 세로로 이동 가능하면
                if room[r + 1][c] == 0:
                    room[r + 1][c] = 2
                    move_the_pipe(r + 1, c, 2)
                    room[r + 1][c] = 0

                # 만약에 대각으로 이동 가능하면
                if room[r][c + 1] == 0 and room[r + 1][c + 1] == 0 and room[r + 1][c] == 0:
                    room[r][c + 1], room[r + 1][c + 1], room[r + 1][c] = 2, 2, 2
                    move_the_pipe(r + 1, c + 1, 3)
                    room[r][c + 1], room[r + 1][c + 1], room[r + 1][c] = 0, 0, 0

        # pipe_status가 대각선
        elif pipe_status == 3:

            if room[r][c + 1] != 0 and room[r + 1][c + 1] != 0 and room[r + 1][c] != 0:
                return

            else:
                # 만약에 가로로 이동 가능하면
                if room[r][c + 1] == 0:
                    room[r][c + 1] = 2
                    move_the_pipe(r, c + 1, 1)
                    room[r][c + 1] = 0

                # 만약 세로로 이동 가능하면
                if room[r + 1][c] == 0:
                    room[r + 1][c] = 2
                    move_the_pipe(r + 1, c, 2)
                    room[r + 1][c] = 0

                # 만약에 대각으로 이동 가능하면
                if room[r][c + 1] == 0 and room[r + 1][c + 1] == 0 and room[r + 1][c] == 0:
                    room[r][c + 1], room[r + 1][c + 1], room[r + 1][c] = 2, 2, 2
                    move_the_pipe(r + 1, c + 1, 3)
                    room[r][c + 1], room[r + 1][c + 1], room[r + 1][c] = 0, 0, 0

# 방의 크기
N = int(input())
# 방의 정보
# 0은 이동 가능 / 1은 벽이라 불가능
room = [[2] * (N + 2)] + [ [2] + list(map(int, input().split())) + [2] for _ in range(N) ] + [[2] * (N + 2)]

room[1][1], room[1][2] = 2, 2

# 가능한 횟수
cnt = 0
# 가로는 1, 세로는 2, 대각선은 3
# 초기 값은 1
move_the_pipe(1, 2, 1)

print(cnt)