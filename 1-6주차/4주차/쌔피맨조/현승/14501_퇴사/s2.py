# dfs로 해보기
import sys

sys.stdin = open("input.txt", "r")
import time

start = time.time()

def dfs(day, total):
    global answer
    if day == N+1:
        if answer < total:
            answer = total
        return
    elif day > N+1:
        return

    if answer < total:
        answer = total

    dfs(day+1, total)
    dfs(day + T[day], total + P[day])


N = int(input())
T = [0 for _ in range(N + 1)]
P = [0 for _ in range(N + 1)]
dp = [0 for _ in range(N + 2)]
for i in range(1, N + 1):
    T[i], P[i] = map(int, input().split())

answer = 0
dfs(1, 0)
print(answer)

print("time: ", time.time() - start)