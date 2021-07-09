import sys
import copy

# 3016ms pypy
sys.stdin = open('input.txt')



def getArea(): # 초기값 구하기
    safe = 0 # 안전지대의 수
    virus = [] # 바이러스의 위치
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                safe += 1
            if arr[i][j] == 2:
                virus.append((i, j))
    return safe, virus


def BFS(): # 바이러스 퍼트리기
    global MIN

    wall = copy.deepcopy(arr) # 2차원 배열 복사
    que = list(virus) # 바이러스로 큐 초기화
    cnt = 0 # 바이러스가 퍼진 빈칸 수

    while que:
        if cnt > MIN: # 백트래킹 : 최소보다 커지면 그만
            return

        r, c = que.pop(0)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M:
                if wall[nr][nc] == 0:
                    cnt += 1
                    wall[nr][nc] = 2
                    que.append([nr, nc])

    MIN = min(MIN, cnt)


def setWall(idx): # 벽 3개 모든 조합
    if idx == 3:
        BFS()
        return
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                arr[i][j] = 1
                setWall(idx+1)
                arr[i][j] = 0

N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
MIN = 100

safe, virus = getArea()
setWall(0)
print(safe - MIN - 3)