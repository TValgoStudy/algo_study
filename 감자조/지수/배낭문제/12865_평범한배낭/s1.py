import sys
sys.stdin = open('input.txt')
q = lambda : map(int, sys.stdin.readline().split())

N, V = q()
items = [list(q()) for _ in range(N)]
DP = [0] * (V+1)
MAX = 0

def getItem(idx, weight, value):
    global MAX

    if idx == N:
        MAX = max(value, MAX)
        return

    if value < DP[weight]:
        return

    DP[weight] = value

    getItem(idx+1, weight, value)

    if weight + items[idx][0] <= V:
        getItem(idx+1, weight + items[idx][0], value + items[idx][1])


getItem(0, 0, 0)
print(MAX)


