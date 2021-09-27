from sys import stdin
input = stdin.readline


def update(y, x):
    global shark
    sy, sx, v, l = shark
    fish_map[y][x] = 0
    shark = [y, x, v+1, v+1] if l == 1 else [y, x, v, l-1]


def bfs():
    global shark
    sy, sx, v, _ = shark
    visited = [[0]*N for _ in range(N)]
    visited[sy][sx] = 1
    queue = [(sy, sx)]
    depth = 0
    while queue:
        depth += 1
        can_eat_fishes = []
        len_q = len(queue)
        for _ in range(len_q):
            y, x = queue.pop(0)
            # 4방 탐색
            for nxt_y, nxt_x in ((y-1, x), (y, x-1), (y, x+1), (y+1, x)):
                if (0 <= nxt_y < N and 0 <= nxt_x < N) and not visited[nxt_y][nxt_x] and fish_map[nxt_y][nxt_x] <= v:
                    visited[nxt_y][nxt_x] = 1
                    if 0 < fish_map[nxt_y][nxt_x] < v:
                        can_eat_fishes.append((nxt_y, nxt_x))
                    else:
                        queue.append((nxt_y, nxt_x))
        if can_eat_fishes:
            fish = sorted(can_eat_fishes)[0]
            update(*fish)
            return depth
    return 0


N = int(input())
fish_map = []
shark = []
start_flag = False
for y in range(N):
    row = list(map(int, input().split()))
    for x, v in enumerate(row):
        if v == 9:
            # y, x, size, life
            shark = [y, x, 2, 2]
        elif not start_flag and v != 0:
            start_flag = (v < 2)
    fish_map.append(row)
fish_map[shark[0]][shark[1]] = 0
time = 0
if start_flag:
    while True:
        # bfs 성공하면 time 연산
        tmp_time = bfs()
        if not tmp_time:
            break
        time += tmp_time
print(time)
