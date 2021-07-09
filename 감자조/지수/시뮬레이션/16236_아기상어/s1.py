import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# 물고기 M마리, 상어 1마리
# 처음 아기 상어 크기 2
# 작은 물고기만 먹을 수 있음
# 자신의 크기의 수만큼 먹으면 크기 +1

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]


def findShark(): # 초기 상어 위치 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 9:
                arr[i][j] = 0
                return i, j



def BFS():
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    r, c = findShark()

    que = [(r, c, 0)]
    size = 2 # 상어 크기
    canEat = set() # 먹을 수 있는 생선 위치

    dist = 0 # 상어~생선 최소 거리
    time = 0 # 전체 이동 시간
    eatCnt = 0 # 현재 사이즈에서 잡아먹은 생선 수

    visit = [[0] * N for _ in range(N)] # 이동 위치 체크

    while que:
        r, c, d = que.pop(0)
        visit[r][c] = 1

        if dist and d >= dist: # 아래에서 최소 거리가 구해진 경우(잡아먹을 생선 있는 경우)
            canEat = list(canEat) # 리스트로 변경
            canEat.sort(key = lambda x: (x[0], x[1])) # 위, 왼쪽 정렬

            fr, fc, d = canEat[0] # 먹을 생선
            arr[fr][fc] = 0 # 먹기
            eatCnt += 1 # 먹은 횟수 + 1
            time += d # 이동 거리(시간)

            if eatCnt >= size: # 성장
                size += 1
                eatCnt = 0

            # 초기화
            canEat = set()
            que = [(fr, fc, 0)]
            dist = 0
            visit = [[0] * N for _ in range(N)]
            continue


        for k in range(4): # 4방 이동
            nr, nc = r + dr[k], c + dc[k]

            if not (0 <= nr < N and 0 <= nc < N): # 범위 넘어갔거나
                continue

            if arr[nr][nc] > size: # 갈 수 없거나
                continue

            if visit[nr][nc]: # 갔던 곳은 스킵
                continue

            que.append((nr, nc, d+1)) # 거리+1 해서 큐에 추가
            visit[nr][nc] = 1 # 방문 체크

            if 0 < arr[nr][nc] < size: # 잡아 먹을 수 있으면
                dist = d + 1 # 최소거리에 기록 (BFS니까 가능)
                canEat.add((nr, nc, d+1)) # 잡아먹을 후보에 추가


    return time


print(BFS())