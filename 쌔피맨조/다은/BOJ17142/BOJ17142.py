import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame
from itertools import combinations


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dfs(virus: tuple, IN_copy: list):
    q = list(virus)
    while q:
        r, c = q.pop(0)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N and (not IN_copy[nr][nc] or IN_copy[nr][nc] == '*'):
                IN_copy[nr][nc] = IN_copy[r][c] + 1
                q.append((nr, nc))

    dfs_result = 0
    for r in range(N):
        for c in range(N):
            # 모든 빈 칸에 바이러스를 못 퍼뜨리면 -1
            if not IN_copy[r][c]:
                return -1

            # 비활성 바이러스면 그냥 넘기기
            if IN_copy[r][c] == '*' or IN[r][c] == '*':
                continue

            # 모든 빈칸에 바이러스를 퍼뜨렸으면 max값을 찾는다
            if IN_copy[r][c] > dfs_result:
                dfs_result = IN_copy[r][c]

    return dfs_result


N, M = map(int, input().split())
IN = [list(map(int, input().split())) for _ in range(N)]
viruses = []

result = 0
for r in range(N):
    for c in range(N):
        # 바이러스는 viruses에 넣고 다 비활성 상태로 바꿈
        if IN[r][c] == 2:
            viruses.append((r, c))
            IN[r][c] = '*'
    # 바이러스 없는 빈 칸이 있으면 dfs 실행할 예정 result 초기값 설정
    if 0 in IN[r]:
        result = 999999999

# 처음부터 빈 칸이 없으면 0 출력
if result == 0:
    print(0)
# 빈 칸이 있으면 dfs 실행
else:
    # combinations으로 viruses 리스트에서 M개 뽑기
    for virus in combinations(viruses, M):
        # IN을 copy하고 특정 바이러스만 활성 상태로 바꾸기
        IN_copy = [i[:] for i in IN]
        for r, c in virus:
            IN_copy[r][c] = 2
        # dfs 실행
        tmp = dfs(virus, IN_copy)
        # 바이러스를 퍼뜨리는 최소 시간 찾기
        if tmp != -1:
            result = min(result, tmp)

    # 모든 빈 칸에 바이러스 퍼뜨리는 경우가 없으면 -1
    if result == 999999999:
        print(-1)
    # 있으면 첫 시작이 2이니까 2 빼고 출력
    else:
        print(result-2)
