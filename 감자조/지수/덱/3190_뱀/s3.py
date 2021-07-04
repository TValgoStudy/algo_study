import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
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