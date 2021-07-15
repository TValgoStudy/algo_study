import sys
sys.stdin = open("input.txt", "r")

from collections import deque

def bfs(i, arr_tmp):
    visited = [[0 for _ in range(M)] for _ in range(N)]
    q = deque([(N, i)])
    cnt = -1
    while q:
        cnt += 1
        if cnt == D:
            break
        candidates = []
        for _ in range(len(q)):
            x, y = q.popleft()
            for dx, dy in [(0, -1), (-1, 0), (0, 1)]:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    if arr_tmp[nx][ny] == 1:
                        candidates.append((nx, ny))
                    else:
                        q.append((nx, ny))
        if candidates:
            ret_x, ret_y = -1, 1000
            for x, y in candidates:
                if y < ret_y:
                    ret_x, ret_y = x, y
            return ret_x, ret_y

    return -1, -1


def dfs(i, cnt):
    global ans
    if cnt == 3:
        # 실험해볼 배열 복사하기
        arr_tmp = [ar[:] for ar in arr]
        total = 0
        archers = []
        for x in range(M):
            if check[x]:
                archers.append(x)


        # 적이 모두 없어질 때까지? 아니면 행의 개수만큼? 일단 행의 개수만큼
        for row in range(N):
            # 궁수마다 쏜 적 저장
            targets = []
            for archer_idx in archers:
                # 가장 가까운 적 중 가장 왼쪽에 있는 타겟의 좌표를 반환한다.
                x, y = bfs(archer_idx, arr_tmp)
                if (x, y) != (-1, -1):
                    targets.append((x, y))
            # 적 지우기
            for x, y in targets:
                arr_tmp[x][y] = 0

            # arr_tmp 한 칸씩 내리기, 내리면서 성에 도달한 애들 카운트 근데 답보다 많아지면 return
            for j in range(M):
                if arr_tmp[N-1][j] == 1:
                    total += 1
            if total > ans:
                return

            for i in range(N-2, -1, -1):
                for j in range(M):
                    arr_tmp[i+1][j] = arr_tmp[i][j]
            for j in range(M):
                arr_tmp[0][j] = 0

        if total < ans:
            ans = total
        return
    # 시뮬레이션 부분

    # 조합 조합 어떻게 하더라;
    for idx in range(i, M + cnt - 2):
        check[idx] = 1
        dfs(idx+1, cnt+1)
        check[idx] = 0

# idea
# 제거할 수 있는 최대 적의 수 = 성에 도달하는 최소 적의 수 => 가지치기 가능 => 백트래킹으로
N, M, D = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

enemies_cnt = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            enemies_cnt += 1

ans = 9876543210
check = [0 for _ in range(M)]
dfs(0, 0)
print(enemies_cnt - ans)
