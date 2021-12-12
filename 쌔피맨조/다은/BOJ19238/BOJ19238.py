import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs_people(s: tuple, matrix: list):
    q = [s]
    if matrix[s[0]][s[1]] == 2:
        return (s[0], s[1], 0)
    matrix[s[0]][s[1]] = 10
    result = []
    while q:
        r, c = q.pop(0)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            # 이동할 수 있으면 이동하기
            if 0 <= nr < N and 0 <= nc < N and (matrix[nr][nc] == 0 or matrix[nr][nc] == 2):
                if result and result[0][2] < matrix[r][c] + 1 - 10:
                    break
                # 만약 승객이면 태우기
                if matrix[nr][nc] == 2:
                    result.append((nr, nc, matrix[r][c] + 1 - 10))
                q.append((nr, nc))
                matrix[nr][nc] = matrix[r][c] + 1
    # 가장 왼쪽 위에 위치한 승객 탑승
    if result:
        result.sort(key=lambda x: (x[0], x[1]))
        return result[0]

    return (-1, -1, -1)

def bfs_end(s: tuple, e: tuple, matrix: list):
    q = [s]
    matrix[s[0]][s[1]] = 10
    while q:
        r, c = q.pop(0)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            # 이동할 수 있으면 이동하기
            if 0 <= nr < N and 0 <= nc < N and (matrix[nr][nc] == 0 or matrix[nr][nc] == 3):
                # 도착지면 끝
                if (nr, nc) == e:
                    return (nr, nc, matrix[r][c] + 1 - 10)
                q.append((nr, nc))
                matrix[nr][nc] = matrix[r][c] + 1
    # 도착지 도착 불가
    return (-1, -1, -1)




N, M, oil = map(int, input().split())
matrix_p = [list(map(int, input().split())) for _ in range(N)]
matrix_e = [i[:] for i in matrix_p]
endpoint = [[0]*N for _ in range(N)]
r, c = map(int, input().split())
r -= 1; c -= 1

# 벽은 1, 사람은 2, 도착지는 3
for _ in range(M):
    sr, sc, er, ec = map(int, input().split())
    matrix_p[sr-1][sc-1] = 2
    matrix_e[er-1][ec-1] = 3
    # sr-1, sc-1 위치에 있는 승객의 도착지 er-1, ec-1
    endpoint[sr-1][sc-1] = (er-1, ec-1)
# print(DataFrame(matrix_p))
# print(DataFrame(matrix_e))
ok = 0
while ok != M:
    matrix_p_copy = [i[:] for i in matrix_p]

    # 승객 찾기
    tr, tc, dist = bfs_people((r, c), matrix_p_copy)
    # print(tr, tc)
    matrix_p[tr][tc] = 0
    # 승객한테 갈 수 없으면 종료
    if tr == -1 or dist > oil:
        break
    # 갈 수 있으면 위치 갱신, 오일 갱신
    r, c = tr, tc
    oil -= dist

    matrix_e_copy = [i[:] for i in matrix_e]
    # 승객의 목적지 찾기
    tr, tc = endpoint[r][c]
    tr, tc, dist = bfs_end((r, c), (tr, tc), matrix_e_copy)
    # 목적지까지 갈 수 없으면 종료
    if tr == -1 or dist > oil:
        break
    # 갈 수 있으면 위치 갱신, 오일 갱신
    r, c = tr, tc
    # print(tr, tc)
    # print()
    oil -= dist

    # 한명 완료
    oil += dist * 2
    ok += 1

if ok == M:
    print(oil)
else:
    print(-1)
