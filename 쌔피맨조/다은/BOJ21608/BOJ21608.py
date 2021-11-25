import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def func1(me, like):
    result = []
    result_cnt = 0
    for r in range(N):
        for c in range(N):
            if matrix[r][c]:
                continue

            # 해당 matrix r, c 좌표에서 좋아하는 학생 수 체크
            like_cnt = 0
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < N and 0 <= nc < N and matrix[nr][nc] in like:
                    like_cnt += 1

            # r, c에서 like_cnt 개수에 따라 result 갱신
            if like_cnt == result_cnt:
                result.append((r, c))
            elif like_cnt > result_cnt:
                result_cnt = like_cnt
                result = [(r, c)]

    result2 = 0
    result2_cnt = 0
    for r, c in result:
        # matrix r, c 에서 인접한 칸 중 비어있는 칸 세기
        blank_cnt = 0
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N and not matrix[nr][nc]:
                blank_cnt += 1

        # 비어있는 칸이 더 많을 때만 갱신
        if result2_cnt < blank_cnt or not result2:
            result2_cnt = blank_cnt
            result2 = (r, c)

    return result2


N = int(input())
matrix = [[0]*N for _ in range(N)]
student_like = [0] * (N*N + 1)

for _ in range(N*N):
    like = list(map(int, input().split()))
    me = like.pop(0)
    student_like[me] = like  # 뒤에 계산을 위해서 저장

    r, c = func1(me, like)
    matrix[r][c] = me

answer = 0
for r in range(N):
    for c in range(N):
        me = matrix[r][c]
        cnt = 0
        # 4방 탐색하면서 확인
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N and (matrix[nr][nc] in student_like[me]):
                cnt += 1
        if cnt:
            answer += 10 ** (cnt - 1)

print(answer)

