import sys
from heapq import heappop, heappush
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
M = int(input())

cost = [[] for _ in range(N+1)]

for _ in range(M):
    s, e, w = map(int, input().split())
    cost[s].append((w, e))

A, B = map(int, input().split())

def dijkstra(A, B):
    fee = [987654321] * (N+1)
    heap = [(0, A)]

    while heap:
        A_v_pay, v = heappop(heap)

        for v_w_pay, w in cost[v]:
            A_w_pay = A_v_pay + v_w_pay
            if A_w_pay < fee[w]:
                fee[w] = A_w_pay
                heappush(heap, (A_w_pay, w))

    return fee[B]

print(dijkstra(A, B))