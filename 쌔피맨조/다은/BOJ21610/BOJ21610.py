import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame

dr = [0, -1, -1, -1, 0, 1, 1, 1]
dc = [-1, -1, 0, 1, 1, 1, 0, -1]
drc = [(-1, -1), (-1, 1), (1, 1), (1, -1)]

def cloud_move(d: int, s: int, old_cloud: list):
    increase_bucket = []

    while old_cloud:
        r, c = old_cloud.pop()

        # 1. 구름이 d방향으로 s칸 이동
        nr = (r + dr[d] * s) % N
        nc = (c + dc[d] * s) % N

        # 2. 비가 내려서 물 1증가
        matrix[nr][nc] += 1
        # 물이 증가한 칸 체크
        increase_bucket.append((nr, nc))

    # 3. while 종료 : 구름이 모두 사라진다

    # 4. 물 복사 마법 시전
    increase_bucket_copy = increase_bucket[:]
    while increase_bucket_copy:
        r, c = increase_bucket_copy.pop()
        cnt = 0
        for ddr, ddc in drc:
            nr = r + ddr
            nc = c + ddc
            # 범위 내이고, 거리가 1인 칸에 물이 있으면 cnt +1
            if 0 <= nr < N and 0 <= nc < N and matrix[nr][nc]:
                cnt += 1
        matrix[r][c] += cnt

    # 5. 저장된 물의 양이 2 이상인 칸에 구름 생기고 2 줄어든다.
    # 단, 3에서 사리진 칸이 아니어야 함 = increase_bucket 아닌 곳
    new_cloud = []
    for r in range(N):
        for c in range(N):
            if matrix[r][c] >= 2 and (r, c) not in increase_bucket:
                new_cloud.append((r, c))
                matrix[r][c] -= 2

    return new_cloud


N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
cloud = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]

for _ in range(M):
    d, s = map(int, input().split())
    cloud = cloud_move(d-1, s, cloud)

result = 0
for r in range(N):
    result += sum(matrix[r])
print(result)
