import sys
sys.stdin = open("input5.txt", "r")

from itertools import combinations

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for ARR in range(N)]
cnt_max = 0


def blocking(list):
    global virus_max
    # arr 복사
    arr_new = [i[:] for i in arr]
    # i로부터 좌표 위치 추출 및 벽 생성
    for i in list:
        a = i // 8
        b = i % 8
        arr_new[a][b] = 1
    # 바이러스 복사
    virus2 = virus[:]
    cnt = 0
    cntt = dfs(arr_new, virus2, cnt)
    # 최댓값 갱신
    if cntt < virus_max:
        virus_max = cntt

# 바이러스 확산
def dfs(arr_new, vir, cnt):
    global virus_max

    while vir:
        z = vir.pop()
        node_y = z // 8
        node_x = z % 8
        if virus_max <= cnt:
            return 64
        for i in range(4):
            ny = node_y + dy[i]
            nx = node_x + dx[i]
            if 0 <= nx < M and 0 <= ny < N and arr_new[ny][nx] == 0:
                vir.append(ny * 8 + nx)
                arr_new[ny][nx] = 2
                cnt += 1

    return cnt


# 벽을 세울 수 있는 후보군 찾기
possible_block = []
virus = []
safe_zone = 0
virus_max = 64
for y in range(N):
    for x in range(M):
        if arr[y][x] == 0:
            possible_block.append(y * 8 + x)
            safe_zone += 1
        elif arr[y][x] == 2:
            virus.append(y * 8 + x)
block_3_list = combinations(possible_block, 3)

for i in block_3_list:
    blocking(i)

print(safe_zone - virus_max - 3)