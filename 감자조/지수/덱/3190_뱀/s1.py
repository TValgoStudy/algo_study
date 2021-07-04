import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
K = int(input())
apples = []
for _ in range(K):
   y, x =  map(int, input().split())
   apples.append([y-1, x-1])

L = int(input())
moves = []
for _ in range(L):
    info = input().split()
    if info:
        sec, d = info[0], info[1]
        moves.append([int(sec), d])

def snakeMove():

    # D 나오면 +1, L 나오면 -1
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    snake = deque()
    snake.appendleft((0, 0))  # 머리 추가, 꼬리 자르기
    k = 0
    result = 1

    for time, direction in moves:
        time = int(time) - result

        for go in range(time):
            r, c = snake[0] # 머리
            result += 1

            if 0 <= r + dr[k] < N and 0 <= c + dc[k] < N: # 이동 가능하면
                nr = r + dr[k] # 이동
                nc = c + dc[k] # 이동

                if (nr, nc) in snake:
                    return result
                else:
                    snake.appendleft((nr, nc))

                if [nr, nc] in apples:
                    apples.remove([nr, nc]) # 사과먹기, 꼬리 그대로
                else:
                    snake.pop() # 꼬리 자르기


            else: # 이동 불가 == 벽
                return result

        if direction == 'D':
            k += 1
            if k == 4: k = 0
        else:
            k -= 1
            if k == -1: k = 3


    if k == 0:
        result += N - snake[0][1]
    elif k == 1:
        result += N - snake[0][0]
    elif k == 2:
        result += snake[0][1] + 1
    else:
        result += snake[0][0] + 1

    return result

print(snakeMove())