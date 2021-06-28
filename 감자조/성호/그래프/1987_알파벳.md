# 1987 알파벳



## 나의 풀이(pypy3 통과)

```python
import sys
sys.stdin = open('input.txt')

# 세로 R칸, 가로 C칸
# 상하좌우 인접 칸으로 이동 가능, 이동한 칸의 알파벳은 새로운 알파벳이어야 함
# 좌측 상단에서 시작한 말이 최대 몇 칸을 지나는가?(시작점 포함)
# R과 C는 최대 20으로, 그렇게 크지는 않다.
# 백트래킹을 어떻게 할지??
def dfs(r, c, cnt):
    global max_cnt
    if max_cnt < cnt:
        max_cnt = cnt

    for k in range(4):
        # 새로 방문하고자 하는 좌표
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < R and 0 <= nc < C:
            if not visited[nr][nc] and not alpha[ord(board[nr][nc])]:
                alpha[ord(board[nr][nc])] = 1  # 방문 처리
                visited[nr][nc] = 1
                dfs(nr, nc, cnt+1)
                alpha[ord(board[nr][nc])] = 0  # 방문 처리 풀기
                visited[nr][nc] = 0

R, C = map(int, input().split())

board = [list(input()) for _ in range(R)]
visited = [[0]*C for _ in range(R)]
alpha = [0]*200 # A~Z까지 방문한 알파벳을 기록할 배열

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 초기화
max_cnt = 0
visited[0][0] = 1
alpha[ord(board[0][0])] = 1

dfs(0, 0, 1)
print(max_cnt)

# 6316ms
```

다시 풀어보면서 통과는 했는데, pypy3로 6316ms(속도 순위 371명/757명)나 걸렸다. 백트래킹을 어떻게 해야할지 고민이 된다.



## 다른 사람의 풀이([gkgg123](https://www.acmicpc.net/user/gkgg123))

```python
R,C = map(int,input().split())

arr = [list(input()) for _ in range(R)]
check = [['']*C for _ in range(R)]

stack = [(0,0,1,arr[0][0])] # 처음: [(0, 0, 1, 'C')]
result = 0
dx = [-1,1,0,0]
dy = [0,0,1,-1]
while stack:
    x,y,cnt,total = stack.pop() # x = 0, y = 0, cnt = 1, total = 'C'
    if result < cnt:
        result = cnt
    if result == 26: # 백트래킹
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < R and 0<= ny <C:
            if arr[nx][ny] not in total:
                # total에는 지금까지 나온 알파벳이 순서대로 저장됨
                # ex) 'C' => 'CA' => 'CAD', ...
                temp = total + arr[nx][ny]
                if check[nx][ny] != temp:
                    check[nx][ny] = temp
                    stack.append((nx,ny,cnt+1,temp))
print(result)

# 208ms
```



알파벳이 26개인 것을 이용하여 백트래킹을 하였다. 이미 최댓값에 도달한 경우에만 더 이상 코드를 진행하지 않음.

=> 내 코드에 적용해 보았지만 while문이 아니라 재귀를 써서 return을 해야 했고, 속도에 큰 차이는 없었다. (6044ms) 웬만하면 while문을 사용하는게 좋겠다.

