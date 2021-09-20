import sys
from pandas import DataFrame
sys.stdin = open("input.txt", "r")


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs_union(r, c, union_num):
    q = [(r, c)]
    IN_open[r][c] = union_num
    while q:
        r, c = q.pop(0)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N and not IN_open[nr][nc]:
                # 인구 차이가 L명 이상, R명 이하라면
                if L <= abs(IN[r][c] - IN[nr][nc]) <= R:
                    q.append((nr, nc))
                    IN_open[nr][nc] = union_num


N, L, R = map(int, input().split())
IN = [list(map(int, input().split())) for _ in range(N)]
result = 0
flag = 1

while flag:
    # 연합 번호
    union_num = 0
    IN_open = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            # 국경 오픈했는지 체크 안된 곳이면 체크하러
            if not IN_open[r][c]:
                union_num += 1
                bfs_union(r, c, union_num)
                # 종료 조건
                if union_num == N*N:
                    flag = 0
    if not flag:
        break

    # 연합 번호에 소속된 총 인구 & 지역 넓이
    union_num_people = [0] * (union_num + 1)
    union_num_region = [0] * (union_num + 1)
    for r in range(N):
        for c in range(N):
            num = IN_open[r][c]
            people = IN[r][c]
            union_num_people[num] += people
            union_num_region[num] += 1

    # 연합 번호의 다음 인구 평균
    union_num_mean = [0] * (union_num + 1)
    for i in range(union_num + 1):
        if union_num_region[i]:
            union_num_mean[i] = union_num_people[i] // union_num_region[i]

    # IN에 인구 재할당
    for r in range(N):
        for c in range(N):
            num = IN_open[r][c]
            IN[r][c] = union_num_mean[num]

    result += 1

print(result)

