# 문제 풀이과정
'''
1. 벽을 선택한다.
2. 바이러스를 퍼트린다.
3. 바이러스가 퍼지지 않은 안전지역 면적을 구한다.
1~3번의 과정을 벽을 선택하는 모든 경우의 수에 대해서 반복하고,
마지막에 안전지역의 max값 리턴
'''

# input 및 변수선언

import sys
import copy

input = sys.stdin.readline

N, M = map(int, input().strip().split())
matrix = []

# N만큼 반복해서 매트릭스에 넣음
for i in range(N):
    L = list(map(int, input().strip().split()))
    matrix.append(L)

# 방향델타 상 우 하 좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

max_value = 0
# 바이러스 체크 리스트
v_list = []
# 매트릭스 돌면서
for i in range(N):
    for j in range(M):
        # 2면 바이러스 리스트에 추가
        if matrix[i][j] == 2:
            v_list.append([i, j])


# 벽 고르기
def select_wall(start, count):
    global max_value
    if count == 3:  # 종료조건, 벽 3개 선택 완료
        sel_NM = copy.deepcopy(matrix)  # deepcopy로 벽이 선택된 배열 복사
        for num in range(len(v_list)):
            r, c = v_list[num]
            spread_virus(r, c, sel_NM)
        safe_counts = sum(i.count(0) for i in sel_NM)  # clean 지역 count
        max_value = max(max_value, safe_counts)
        return True
    else:
        for i in range(start, N * M):  # 2차원 배열에서 조합 구하기
            r = i // M
            c = i % M
            if matrix[r][c] == 0:  # 안전영역인 경우 벽으로 선택가능
                matrix[r][c] = 1  # 벽으로 변경
                select_wall(i, count + 1)  # 벽선택
                matrix[r][c] = 0


def spread_virus(r, c, sel_NM):
    if sel_NM[r][c] == 2:
        # 상하좌우 4방향을 확인하고 범위를 벗어나거나, 벽을만날때까지 반복
        for dir in range(4):
            n_r = r + dr[dir]
            n_c = c + dc[dir]
            if n_r >= 0 and n_c >= 0 and n_r < N and n_c < M:  # 범위를 벗어나지 않을때
                if sel_NM[n_r][n_c] == 0:
                    sel_NM[n_r][n_c] = 2
                    spread_virus(n_r, n_c, sel_NM)


# 메인
select_wall(0, 0)
print(max_value)
