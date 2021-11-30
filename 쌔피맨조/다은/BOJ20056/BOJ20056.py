import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame

def go(r, c):
    while matrix[r][c]:
        # 하나의 파이어볼 뽑아서
        m, s, d = matrix[r][c].pop()

        # 다음 위치 계산
        nr = (r + s * dr[d]) % N
        nc = (c + s * dc[d]) % N

        # 다음위치 갱신
        next_matrix[nr][nc].append((m, s, d))

def division():
    for r in range(N):
        for c in range(N):

            # 파이어볼 1개 이하면 패스
            if len(matrix[r][c]) < 2:
                continue

            # 2개 이상이면 합치기
            total_m, total_s, total_cnt = 0, 0, 0
            even_cnt, odd_cnt = 0, 0
            for m, s, d in matrix[r][c]:
                total_m += m
                total_s += s
                total_cnt += 1
                # 홀수면 odd +1, 짝수면 even +1
                if d % 2:
                    odd_cnt += 1
                else:
                    even_cnt += 1

            division_m = total_m // 5
            division_s = total_s // total_cnt

            # cnt가 둘 다 있으면 방향이 모두 홀수 or 모두 짝수가 아님
            if even_cnt * odd_cnt:
                next_d = [1, 3, 5, 7]
            else:
                next_d = [0, 2, 4, 6]

            # 질량이 있으면
            if division_m:
                matrix[r][c] = []
                for d in next_d:
                    matrix[r][c].append((division_m, division_s, d))
            # 질량이 없으면 소멸
            else:
                matrix[r][c] = []


N, M, K = map(int, input().split())
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]
matrix = [[[] for _ in range(N)] for _ in range(N)]

for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    matrix[r-1][c-1] = [(m, s, d)]

while K:
    next_matrix = [[[] for _ in range(N)] for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if matrix[r][c]:
                go(r, c)
    matrix = next_matrix
    division()
    K -= 1


result = 0
for r in range(N):
    for c in range(N):
        while matrix[r][c]:
            m, s, d = matrix[r][c].pop()
            result += m
print(result)
