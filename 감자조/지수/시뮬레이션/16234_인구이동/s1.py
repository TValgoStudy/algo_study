# python 7812ms
# pypy 1160ms


import sys
sys.stdin = open('input.txt')
q = lambda : map(int, sys.stdin.readline().split())


def solution():
    global visit

    cnt = 0 # 인구이동 횟수

    while True:
        visit = [[0 for _ in range(N)] for __ in range(N)] # 초기화
        linked = [] # 초기화

        for r in range(N):
            for c in range(N):
                if visit[r][c]: continue # 방문한 마을 스킵

                ans = BFS(r, c) # 방문하지 않은 마을 BFS로 인접 마을 확인

                if ans: # 연합이 있으면
                    linked.append(ans) # 연합 결과 기록

        if not linked: break # 아무 연합도 없으면 반복 종료

        cnt += 1

        for val, group in linked:
            for i, j in group:
                arr[i][j] = val # 연합 결과로 인구수 n빵

    return cnt



def BFS(r, c):
    global visit

    que = [(r, c)]
    group = [(r, c)] # 연합 마을
    val = arr[r][c] # 연합 마을 총 인원수
    visit[r][c] = 1
    link = 1 # 연합된 마을 수

    while que:
        r, c = que.pop()
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < N and 0 <= nc < N: # 범위체크
                if visit[nr][nc] == 0: # 방문체크
                    if L <= abs(arr[r][c] - arr[nr][nc]) <= R: # 조건체크
                        link += 1
                        que.append((nr, nc))
                        group.append((nr, nc))
                        val += arr[nr][nc]
                        visit[nr][nc] = 1

    if link > 1:
        return [val // link , group]
    else:
        return 0



N, L, R = q()
arr = [list(q()) for _ in range(N)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
visit = [[0 for _ in range(N)] for __ in range(N)]

print(solution())