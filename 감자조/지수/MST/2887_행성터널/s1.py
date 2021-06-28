import sys
from heapq import heappop, heappush
sys.stdin = open('input.txt')

# MST 구하는 방법 : 크루스칼(Union-find), 프림(힙)

N = int(input())
planet = [list(map(int, input().split())) for _ in range(N)]

visit = [0] * N
heap = [(0, 0)]

def findDistance(v):
    for w in range(N):
        if v == w or visit[w]: continue
        dist = 987654321
        for i in range(3):
            dist = min(dist, abs(planet[v][i] - planet[w][i]))
        heappush(heap, (dist, w))
    print(heap)


def Prim():
    node = 0
    cost = 0

    while node < N:
        d, v = heappop(heap)

        if visit[v]: continue

        visit[v] = 1
        node += 1
        cost += d

        findDistance(v)

    return cost


print(Prim())

