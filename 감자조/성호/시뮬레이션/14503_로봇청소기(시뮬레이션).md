# 14503_로봇청소기

## 내 풀이

```python
def dfs(r, c, d, cnt):
    global max_cnt
    global flag
    if flag:
        return
    if cnt > max_cnt:
        max_cnt = cnt

    room[r][c] = 2 # 1. 현재 위치를 청소한다. (청소는 2로 표시, 벽은 1)
    for k in list(range(d+1, d+5)):
        k = k % 4
        nr = r + dr[k]
        nc = c + dc[k]
        if room[nr][nc] == 0: # 2_a. 청소하지 않은 공간이 존재
            dfs(nr, nc, k, cnt+1) # 그 방향으로 회전 + 전진
    # 모두 청소가 되어있거나 벽인 경우,
    # 만약 뒤쪽 방향이 벽이 아니라면
    # d의 반대 방향으로 이동, 바라보는 방향은 유지
    nr = r + dr[(d+2) % 4] # 뒤의 좌표
    nc = c + dc[(d+2) % 4]
    if room[nr][nc] != 1: # 벽이 아니면
        dfs(nr, nc, d, cnt) # 현재 바라보는 방향을 유지하면서 뒤로 이동
    else:
        flag = True
        return

N, M = map(int, input().split())
r, c, d = map(int, input().split())
# 0: 북, 1: 서, 2: 남, 3: 동 (주어진 보기와 다름)
dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

flag = False
room = [list(map(int, input().split())) for _ in range(N)]
max_cnt = 0
#dr, dc의 동-서 방향을 반대로 했으므로 d의 방향도 반대로 바꿔준다.
if d == 1:
    d = 3
elif d == 3:
    d = 1
dfs(r, c, d, 1)
print(max_cnt)

# pypy3 132ms
```

모든 경우의 수를 따지는게 아니라 시작점에서 주어진 규칙에 따라 이동했을 때 한번에 갈 수 있는 거리를 세는 것이기 때문에 dfs라고 하기도 뭐하다. 어렵지는 않은 문제지만 일부러 반시계방향으로 확인시켜놓고 북동남서로 dr, dc를 만들게 해서 헷갈리게 하는 문제



