import sys
sys.stdin = open('input.txt')

# 인플루언서랑 비슷

N = int(input())
arr = [0] + list(map(int, input().split()))
tree = [[0 for _ in range(N+1)] for __ in range(N+1)]
visit = [0] * (N+1)
dp = [[0 for _ in range(2)] for __ in range(N+1)]


for _ in range(N-1):
    v, w = map(int, input().split())
    tree[v][w] = 1
    tree[w][v] = 1


def goodVillage(v, isGood, cnt):

    for w in range(1, N+1):
        if tree[v][w] and visit[w] == 0:
            visit[w] = (-1)**isGood
            goodVillage(w, not isGood, cnt+1)


visit[1] = 1
goodVillage(1, True, 1)
print(visit)

visit[1] = -1
goodVillage(1, False, 1)
print(visit)
