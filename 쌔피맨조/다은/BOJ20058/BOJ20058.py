import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(s: tuple):
    q = [s]
    matrix_check[s[0]][s[1]] = 1
    cnt = 1
    while q:
        r, c = q.pop(0)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            # 아직 방문하지 않았고, 얼음이면
            if 0 <= nr < M and 0 <= nc < M and not matrix_check[nr][nc] and matrix[nr][nc]:
                q.append((nr, nc))
                matrix_check[nr][nc] = 1
                cnt += 1
    return cnt

# << 연산자 사용해보기
def ice_rotate(matrix, L):

    def ice_small_rotate(R, C):
        for r in range(dist):
            for c in range(dist):
                next_matrix[R+c][C+(dist-1-r)] = matrix[R+r][C+c]

    def ice_count(r, c):
        cnt = 0
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < M and 0 <= nc < M and matrix[nr][nc]:
                cnt += 1

        # 3개 미만 and 얼음이 있으면 감소
        if cnt < 3 and matrix[r][c]:
            next_matrix[r][c] = matrix[r][c] - 1

    ##############################################

    next_matrix = [[0]*M for _ in range(M)]
    dist = 2 ** L

    # 격자를 나눈 후 회전시키고, matrix로 갱신
    for R in range(0, M, dist):
        for C in range(0, M, dist):
            ice_small_rotate(R, C)
    matrix = [i[:] for i in next_matrix]

    # 얼음이 있는 칸 3개 이상 인접 안하면 -1
    for r in range(M):
        for c in range(M):
            ice_count(r, c)
    return next_matrix


N, Q = map(int, input().split())
M = 2 ** N
matrix = [list(map(int, input().split())) for _ in range(M)]
Ls = list(map(int, input().split()))

for L in Ls:
    matrix = ice_rotate(matrix, L)

result = 0
for r in range(M):
    result += sum(matrix[r])
print(result)

large_ice = 0
matrix_check = [[0]*M for _ in range(M)]
for r in range(M):
    for c in range(M):
        # 아직 방문하지 않았고, 얼음이면
        if not matrix_check[r][c] and matrix[r][c]:
            large_ice = max(large_ice, bfs((r, c)))
print(large_ice)
