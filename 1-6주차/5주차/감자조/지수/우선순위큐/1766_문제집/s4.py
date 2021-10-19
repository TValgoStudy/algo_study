import sys
from heapq import heappop, heappush
sys.stdin = open('input.txt')
q = lambda : map(int, sys.stdin.readline().split())

# 위상정렬 추가

N, M = q()

# 먼저 풀 문제들을 담을 리스트
pre = [[me] for me in range(N+1)]
orders = []

for _ in range(M):
    A, B = q()
    pre[B].append(A)


for __ in range(N):
    for i in range(1, N+1):
        if not pre[i]: continue

        if pre[i] == [i]: # 자기자신인 것 == 선수문제가 없는 것 : 진입차수 0
            orders.append(i) # 순서에 추가
            pre[i] = [] # 비우기
            for j in range(1, N+1): # i와 연결된 간선 제거
                if i in pre[j]:
                    pre[j].remove(i)

print(*orders)


