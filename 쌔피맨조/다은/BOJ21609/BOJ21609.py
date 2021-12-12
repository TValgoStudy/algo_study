import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(s: tuple, color, visit):
    q = [s]
    visit[s[0]][s[1]] = 1
    rainbow_list, block_list = [], []
    while q:
        r, c = q.pop(0)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            # 범위 내, 아직 방문 안했고, 같은 색이거나 무지개 색이면
            if 0 <= nr < N and 0 <= nc < N and not visit[nr][nc] and (color == matrix[nr][nc] or not matrix[nr][nc]):
                visit[nr][nc] = 1
                q.append((nr, nc))
                block_list.append((nr, nc))
                # 무지개 블럭이면 cnt +1
                if not matrix[nr][nc]:
                    rainbow_list.append((nr, nc))
    return block_list, rainbow_list

def block_search_remove():
    global score
    ## 1. 가장 큰 블록 찾기
    matrix_visit = [[0]*N for _ in range(N)]
    search_block_list, search_rainbow_list = [], []
    for r in range(N):
        for c in range(N):
            # 색이 있는 블럭이고 아직 bfs 안했으면
            if matrix[r][c] > 0 and not matrix_visit[r][c]:
                block_list, rainbow_list = bfs((r, c), matrix[r][c], matrix_visit)

                # 1. 기존이 비었으면 갱신 2. 더 큰 블록있으면 갱신
                # 3. 기존거랑 새로운거랑 블록 크기 같으면 무지개 블록 더 많을 때 갱신
                # 3-1. 무지개 블록 개수도 같으면 행, 열 더 클 때 갱신
                if not search_block_list:
                    search_block_list, search_rainbow_list = block_list, rainbow_list
                elif len(search_block_list) < len(block_list):
                    search_block_list, search_rainbow_list = block_list, rainbow_list
                elif len(search_block_list) == len(block_list) and\
                    len(search_block_list) <= len(rainbow_list):
                    search_block_list, search_rainbow_list = block_list, rainbow_list

                # 방문체크 했었던 무지개 블록 풀어주기
                for r, c in rainbow_list:
                    matrix_visit[r][c] = 0

    ## 2. 큰 블록 지우기
    score += len(search_block_list) ** 2
    for r, c in search_block_list:
        matrix[r][c] = -2


def gravity():
    for c in range(N):
        bottom_r = N-1
        while bottom_r:
            # 블록이 있으면 bottom_r -1
            if matrix[bottom_r][c] > -2:
                bottom_r -= 1
                continue

            # 블록이 없으면 중력 : 떨어져야하는 r 찾기
            fall_r = bottom_r - 1
            while fall_r >= 0 and matrix[fall_r][c] == -2:
                fall_r -= 1
            # r이 검정 블럭이면 bottom_r 갱신
            if matrix[fall_r][c] == -1:
                bottom_r = fall_r - 1
            # r이 블럭이면 떨어뜨리기
            elif matrix[fall_r][c] > -1:
                matrix[bottom_r][c], matrix[fall_r][c] = matrix[fall_r][c], -2
                bottom_r -= 1


def rotate(matrix):
    return [list(i) for i in list(zip(*matrix))[::-1]]

def check():
    for r in range(N):
        for c in range(N):
            if matrix[r][c] < 0:
                continue

            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                print(nr, nc)
                if 0 <= nr < N and 0 <= nc < N and (matrix[nr][nc] == 0 or matrix[nr][nc] == matrix[r][c]):
                    return True

    return False


N, M = map(int, input().split())
matrix = [list(map(int, input().split()))]
score = 0

while check():
    block_search_remove()
    gravity()
    matrix = rotate(matrix)
    gravity()

print(score)
