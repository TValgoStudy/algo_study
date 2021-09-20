import sys
from pandas import DataFrame
sys.stdin = open("input.txt", "r")

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def cctv_check(cctv_dir):
    IN_copy = [i[:] for i in IN]

    for l, dir in zip(cctv_list, cctv_dir):
        r, c, num = l
        for i in dir:
            nr = r + dr[i]
            nc = c + dc[i]
            while 1:
                # while문이 끝나서 r, c 가 다른 곳으로 이동했으면 초기화
                if not (0 <= nr < N and 0 <= nc < M) or IN_copy[nr][nc] == 6:
                    r, c, num = l
                    break
                # 감시할 수 있는 공간이면 # 으로 바꿔주기
                elif IN_copy[nr][nc] == 0:
                    IN_copy[nr][nc] = '#'
                # 다음으로 이동
                r, c = nr, nc
                nr = r + dr[i]
                nc = c + dc[i]

    return IN_copy



def func(cctv_idx, cctv_dir):
    global result

    # 방향을 다 정했으면
    if cctv_idx == cctv_cnt:
        # 감시 영역 체크하기
        IN_copy = cctv_check(cctv_dir)

        # 감시 못 하는 영역 세기
        c_result = 0
        for r in range(N):
            for c in range(M):
                if IN_copy[r][c] == 0:
                    c_result += 1
        if c_result < result:
            result = c_result
        return

    # 모든 경우의 수
    if cctv_list[cctv_idx][2] == 1:
        for i in range(4):
            func(cctv_idx+1, cctv_dir + [(i, )])
    elif cctv_list[cctv_idx][2] == 2:
        func(cctv_idx + 1, cctv_dir + [(0, 2)])
        func(cctv_idx + 1, cctv_dir + [(1, 3)])
    elif cctv_list[cctv_idx][2] == 3:
        func(cctv_idx + 1, cctv_dir + [(0, 1)])
        func(cctv_idx + 1, cctv_dir + [(1, 2)])
        func(cctv_idx + 1, cctv_dir + [(2, 3)])
        func(cctv_idx + 1, cctv_dir + [(3, 0)])
    elif cctv_list[cctv_idx][2] == 4:
        func(cctv_idx + 1, cctv_dir + [(0, 1, 2)])
        func(cctv_idx + 1, cctv_dir + [(1, 2, 3)])
        func(cctv_idx + 1, cctv_dir + [(2, 3, 0)])
        func(cctv_idx + 1, cctv_dir + [(3, 0, 1)])
    elif cctv_list[cctv_idx][2] == 5:
        func(cctv_idx + 1, cctv_dir + [(0, 1, 2, 3)])


N, M = map(int, input().split())
IN = [list(map(int, input().split())) for _ in range(N)]

cctv_cnt = 0
cctv_list = []
for r in range(N):
    for c in range(M):
        if IN[r][c] and IN[r][c] != 6:
            cctv_cnt += 1
            cctv_list.append((r, c, IN[r][c]))

result = float('inf')
func(0, [])
print(result)
