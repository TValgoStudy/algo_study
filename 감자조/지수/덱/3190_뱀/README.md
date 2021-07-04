### 내 풀이

1. 이렇게 푼 이유?

   - 뱀 덱을 구성하여 0번인덱스를 머리, -1인덱스를 꼬리로 두었다.
   - 뱀이 이동하면 머리에 dr,dc를 더하여 이동하고, 이동했으니 꼬리 부분은 없앤다.
   
2. 실행시간

   - 96ms (python)

3. 코드

   ```python
   import sys
   from collections import deque
   input = sys.stdin.readline
   
   # 입력
   N = int(input())
   apples = [[0] * N for _ in range(N)]
   
   K = int(input())
   for _ in range(K):
      y, x =  map(int, input().split())
      apples[y-1][x-1] = 1
   
   L = int(input())
   moves = dict()
   for _ in range(L):
       sec, d = input().split()
       moves[int(sec)] = d
   
   
   # 함수
   def snakeMove():
       # D 나오면 +1, L 나오면 -1
       dr = [0, 1, 0, -1]
       dc = [1, 0, -1, 0]
   
       snake = deque()
       snake.appendleft((0, 0))  # 머리 추가, 꼬리 자르기
       k = 0 # 방향
       result = 0
   
       while 1:
           result += 1
           r, c = snake[0] # 머리
   
           if 0 <= r + dr[k] < N and 0 <= c + dc[k] < N: # 이동 가능하면
               nr = r + dr[k] # 이동
               nc = c + dc[k] # 이동
   
               if (nr, nc) in snake: # 몸에 부딛힌 경우
                   return result
               else:
                   snake.appendleft((nr, nc))
   
               if apples[nr][nc]:
                   apples[nr][nc] = 0 # 사과먹기, 꼬리 그대로
               else:
                   snake.pop() # 꼬리 자르기
   
           else: # 이동 불가 == 벽
               return result
   
           if result in moves.keys():
               direction = moves[result]
               if direction == 'D': k += 1
               else: k -= 1
               k %= 4
   
   
   print(snakeMove())
   ```



### 다른 사람의 풀이

1. 실행시간

   - 60ms

2. 코드

   ```python
   import sys
   n = int(sys.stdin.readline())
   apple = set([tuple(map(int, sys.stdin.readline().split())) for i in range(int(sys.stdin.readline()))])
   cmd = [list(sys.stdin.readline().split()) for i in range(int(sys.stdin.readline()))]
   snake = [[-2]*n for _ in range(n)]
   snake[0][0] = 0
   x,y,d = 0,0,0
   l = 1
   t = 0
   idx = 0
   dx = [0,1,0,-1]
   dy = [1,0,-1,0]
   # print((2,5) in apple)
   
   while True:
       t += 1
       l += 1
       x += dx[d]
       y += dy[d]
       if x < 0 or x >= n or y < 0 or y >= n:
           break
       if snake[x][y] >= t-l+1:
           break
       if (x+1,y+1) in apple:
           apple.remove((x+1,y+1))
       else:
           l -= 1
       snake[x][y]=t
   
       if idx < len(cmd) and int(cmd[idx][0]) == t:
           if cmd[idx][1] == 'D':
               d = (d+1) % 4
           else:
               d = (d+3) % 4
           idx += 1
   print(t)
   ```
   
3. 해설

   - 뱀의 위치를 덱이 아니라 2차원 배열로해서 pop, append가 아닌 값을 0,1로 바꾸어서 시간적으로 우세하다.