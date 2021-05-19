# n by n matrix, number of sharks is M, 한칸에 최대 1마리,
# initial size = 2, size is natural number
# 먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다 -> BFS + 같은 거리
#  자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가한다 2면 2마리, 3이면 3마리
# 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.
# 0 1 0 1 0 거리고 같고 가장위에 있고 그 중에 가장 왼쪽 -> min_row, min _col -> 위, 좌, 우, 아래 순 탐색하면 처음 발견에서 break 가능
# 0 0 0 0 1
# 0 0 9 0 0

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

# up, left right, down
dr = [-1, 0, 0, 1]
dc = [0, -1, 1, 0]

shark_size = 2
left_exp = 2
left_fishes = 0
baby_shark_position = (0, 0)
for i in range(N):
    for j in range(N):
        state = matrix[i][j]
        if state:
            if state == 9:
                baby_shark_position = (i, j)
                break
            else:
                left_fishes += 1

T = 0
queue = list()
queue.append(baby_shark_position)
max_iteration_depth = 2*(N-1)
distance = 0
while distance < max_iteration_depth:
    distance = 0
    visited = [[0]*N for _ in range(N)]
    flag = False
    distance += 1
    repeat = len(queue)
    for _ in range(repeat):
        row, col = queue.pop()
        for d in range(4):
            nr = row + dr[d]
            nc = col + dc[d]
            if visited[nr][nc]:
                continue
            if matrix[nr][nc] and matrix[nr][nc] < shark_size:
                baby_shark_position = (nr, nc)
                left_exp -= 1
                if left_exp == 0:
                    shark_size += 1
                    left_exp = shark_size
                    flag = True
                break
            elif matrix[nr][nc] <= shark_size:
                queue.append((nr, nc))
                visited[nr][nc] = 1
        if flag:
            break
    T += distance


print(T)
