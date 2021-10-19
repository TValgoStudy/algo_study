import sys
import copy
from itertools import combinations
sys.stdin = open('input.txt', 'r')

def choose_wall_place(wall_place:list, visited:list, cnt:int, tmp:list):
    if cnt == 3:
        combinations.append(tmp[:])
        return

    for i in range(len(visited)):
        if not(visited[i]):
            tmp.append(wall_place[i])
            visited[i] = 1
            choose_wall_place(wall_place, visited,cnt+1, tmp)
            visited[i] = 0
            tmp.pop()

def spread_virus(lab:list, N:int, M:int):
    for i in range(N):
        for j in range(M):
            if lab[i][j] == 2:
                # 퍼트림
                for k in range(4):
                    nr = i + dr[k]
                    nc = j + dc[k]

                    # 연구실 범위
                    if not(0<=nr<N and 0<=nc<M):
                        continue

                    # 퍼트림
                    if lab[nr][nc] == 0:
                        lab[nr][nc] = 2

def is_it_same(after_matrix:list, before_matrix:list, N:int, M:int):
    for i in range(N):
        for j in range(M):
            if after_matrix[i][j] != before_matrix[i][j]:
                return False
    return True

def count_safe_area(matrix:list, N:int, M:int):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 0:
                cnt += 1
    return cnt
# 0 빈칸, 1 벽, 2 바이러스


N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
# 벽을 세울 장소를 선정해야함
wall_place = []
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 0:
            wall_place.append([i,j])
visited = [0 for _ in range(len(wall_place))]
# combinations = []
combination = list(combinations(wall_place,3))

# choose_wall_place(wall_place, visited, 0, [])


# 두 행렬이 같냐 다르냐
same_flag = False

# 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


max_val = 0
for comb in combination:
    # 첫 복사 -> deepcopy 보다는 for문이 더 빠르다...!
    before_matrix = copy.deepcopy(matrix)
    # 벽세우기
    for i in range(len(comb)):
        wall = comb[i]
        before_matrix[wall[0]][wall[1]] = 1
    after_matrix = copy.deepcopy(before_matrix)

    while not same_flag:
        spread_virus(after_matrix, N, M)
        same_flag = is_it_same(after_matrix, before_matrix, N, M)
        if same_flag:
            answer = count_safe_area(after_matrix, N, M)
            max_val = max(max_val, answer)
        else:
            # answer = count_safe_area(after_matrix, N, M)
            before_matrix = copy.deepcopy(after_matrix)
    same_flag = False

print(max_val)