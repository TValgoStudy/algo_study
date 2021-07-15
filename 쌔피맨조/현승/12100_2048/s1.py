import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame

def in_range(x, y):
    return True if 0 <= x < N and 0 <= y < N else False

def atomic_move(row, col, arr_copy, dr, dc, check, total):
    if arr_copy[row][col]:
        nr, nc = row + dr, col + dc
        while in_range(nr, nc) and arr_copy[nr][nc] == 0:
            nr += dr
            nc += dc
        if in_range(nr, nc):
            if not check[nr][nc] and arr_copy[nr][nc] == arr_copy[row][col]:
                arr_copy[nr][nc] *= 2
                if total < arr_copy[nr][nc]:
                    total = arr_copy[nr][nc]
                arr_copy[row][col] = 0
                check[nr][nc] = 1
            else:
                nr -= dr
                nc -= dc
                if not (nr == row and nc == col):
                    arr_copy[nr][nc] = arr_copy[row][col]
                    arr_copy[row][col] = 0
        else:
            nr -= dr
            nc -= dc
            arr_copy[nr][nc] = arr_copy[row][col]
            arr_copy[row][col] = 0
    return arr_copy, total

def move(dr, dc, total, my_arr):
    arr_copy = [my_arr[i][:] for i in range(N)]
    check = [[0 for _ in range(N)] for _ in range(N)]
    # 합쳐진 친구는 체크
    # 체크되지 않고, 같은 수이면 합칠 수 있음
    # 좌
    if dr == 0 and dc == -1:
        for col in range(1, N):
            for row in range(N):
                arr_copy, total = atomic_move(row, col, arr_copy, dr, dc, check, total)
    # 우
    elif dr == 0 and dc == 1:
        for col in range(N-2, -1, -1):
            for row in range(N):
                arr_copy, total = atomic_move(row, col, arr_copy, dr, dc, check, total)
    # 상
    elif dr == -1 and dc == 0:
        for row in range(1, N):
            for col in range(N):
                arr_copy, total = atomic_move(row, col, arr_copy, dr, dc, check, total)
    # 하
    else:
        for row in range(N-2, -1, -1):
            for col in range(N):
                arr_copy, total = atomic_move(row, col, arr_copy, dr, dc, check, total)

    return arr_copy, total


def dfs(cnt, total, my_arr):
    global ans
    if cnt == 5:
        if ans < total:
            ans = total
        return
    # 가지치기
    # if total * pow(2, 5-cnt) < ans:
    #     return

    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_arr, new_total = move(dx, dy, total, my_arr)
            # print('이동회수 : ', cnt+1)
            # print(DataFrame(new_arr))
            dfs(cnt+1, new_total, new_arr)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
tot = 0
for i in range(N):
    for j in range(N):
       if arr[i][j] > tot:
           tot = arr[i][j]

ans = tot
dfs(0, tot, arr)
print(ans)