#  0은 빈 칸, 1은 벽, 2는 바이러스
# 새로 세울 수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야 한다.
# 대각선으로는 안퍼진다.

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]


# 1. 완전 탐색 추가 벽이 3개 임으로 모든 좌표에 놔보고 최대 갯수를 구한다.
def delta_function(array, row, col):
    # 상 하 좌 우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for d in range(4):
        nr = row + dr[d]
        nc = col + dc[d]
        if 0 <= nr < len(array) and 0 <= nc < len(array[row]) and array[nr][nc] == 0:
            array[nr][nc] = 2
            array = delta_function(array, nr, nc)
    return array


def spread_virus(array):
    for row in range(len(array)):
        for col in range(len(array[row])):
            if array[row][col] == 2:
                array = delta_function(array, row, col)
    return array


def count_safe_area(array):
    cnt = 0
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == 0:
                cnt += 1
    return cnt


def set_wall(array, i, j, n, m, wall=0):
    global answer
    if wall >= 3:
        new_arr = []
        for idx in range(n):
            new_arr.append(array[idx][:])
        infected_area = spread_virus(new_arr)
        tmp = count_safe_area(infected_area)
        if tmp > answer:
            answer = tmp
        return

    for row in range(i, n):
        if row != i:
            j = 0
        for col in range(j, m):
            if array[row][col] == 0:
                array[row][col] = 1
                set_wall(array, row, col, n, m, wall=wall + 1)
                array[row][col] = 0


answer = 0
set_wall(arr, 0, 0, N, M)
print(answer)
