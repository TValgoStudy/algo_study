import sys
from heapq import heappush, heappop

sys.stdin = open('input.txt')
q = lambda: map(int, sys.stdin.readline().split())

# input
N, M = q()

next_problem = [[] for _ in range(N+1)]
pre_problem_cnt = [0] * (N+1)
heap = []

# init
for _ in range(M):
    A, B = q()
    next_problem[A].append(B)
    pre_problem_cnt[B] += 1


# 선수문제가 없는 문제 구하기
for i in range(1, N+1):
    if pre_problem_cnt[i] == 0:
        heappush(heap, i) # 여기선 어차피 앞에서부터 추가해서 heappush랑 같고 더 빠름


# 정렬 & 출력
while heap:
    problem = heappop(heap) # 문제 번호 작은 순(최소힙)
    print(problem, end=" ")

    for np in next_problem[problem]:
        pre_problem_cnt[np] -= 1
        if pre_problem_cnt[np] == 0:
            heappush(heap, np)