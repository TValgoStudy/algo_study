
import sys
import copy
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

# 벽 고르기(조합)
def my_walls(start, wall_count):
    global my_max
    # 벽 세개 골랐으면(종료조건)
    if wall_count == 3:
        # 깊은 복사 (초기 매트릭스 복사)
        copy_matrix = copy.deepcopy(matrix)
        # 복사한 맵 순회하면서
        for r in range(N):
            for c in range(M):
                # 좌표별로 바이러스 퍼트림
                spread_virus(r, c, copy_matrix)
        # 바이러스 퍼트리는 함수 끝나면 바이러스 퍼진 맵을 가지게 됨
        # 청정구역 세기!
        safe_counts = sum(i.count(0) for i in copy_matrix)
        # 청정구역 센거랑, 내가 갖고있던 최대값중에 큰거 골라서 갱신
        my_max = max(safe_counts, my_max)
        return True

    else:
        # 벽 3개 미만이면 조합!
        for i in range(start, N * M):
            r = i // M
            c = i % M
            if matrix[r][c] == 0:  # 안전영역인 경우 벽으로 선택가능
                matrix[r][c] = 1  # 벽으로 변경
                my_walls(i, wall_count + 1)  # 벽선택
                matrix[r][c] = 0

# 전달받은 좌표에다가 바이러스 퍼트리면
def spread_virus(r, c, copy_matrix):
    # 복사한 맵(바이러스 퍼트리는 맵)의 특정 좌표에 바이러스가 있으면(2면)
    if copy_matrix[r][c] == 2:
        # 상하좌우로 퍼져나감! 벽을 만나면 멈춤
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            # 이동한 자리가 범위 안이면 (인덱스 에러 조심!)
            if 0 <= nr < N and 0 <= nc < M:
                # 그리고 아직 바이러스 없는 곳이면!
                if copy_matrix[nr][nc] == 0:
                    # 바이러스 오염!
                    copy_matrix[nr][nc] = 2
                    # 그리고 다시시작
                    spread_virus(nr, nc, copy_matrix)
                # 범위 안이지만 바이러스가 이미 있거나 벽이면 재귀 들어갈 필요 없음



# 시작!
N, M = map(int, input().strip().split())
matrix = []
# 기본 맵정보 받아옴
for i in range(N):
    map_line = list(map(int, input().strip().split()))
    matrix.append(map_line)

# 방향델타 상 우 하 좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# 깨끗한 구역 최댓값 갱신하려고 씀
my_max = 0


my_walls(0, 0)
print(my_max)

