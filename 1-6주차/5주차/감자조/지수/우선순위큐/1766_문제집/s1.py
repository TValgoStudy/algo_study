import sys
sys.stdin = open('input.txt')
q = lambda : map(int, sys.stdin.readline().split())

# 먼저 푸는 것, 쉬운 문제 -> 우선순위
# 우선순위 큐 = 힙?
# 먼저 푸는게 바로 다음에 푼다는 뜻인듯? 바로 다음에 푸는게 아니라면 3-1-4-2도 되야함
# 서로소집합을 만들어서 부모 저장 서로 다른 그룹중에서는 root가 작은 그룹 먼저 풀기

N, M = q()

# 부모(먼저풀문제), 자식(다음에풀문제)
pc = [[i, i] for i in range(N+1)]
orders = []
solved = [0] * (N+1)

def setPC(A, B):
    pc[B][0] = A
    pc[A][1] = B

def findOrder(problem):
    temp = [problem]

    while problem != pc[problem][1]:
        problem = pc[problem][1]
        temp.append(problem)

    orders.append(temp)

def findRoot():
    for j in range(1, N+1):
        if j == pc[j][0]: # 자기자신이 부모이면 root
            findOrder(j)

for _ in range(M):
    A, B = q()
    setPC(A, B)

findRoot()

for __ in range(N):
    min_idx = -1
    min_val = 987654321
    for idx, order in enumerate(orders):
        if order and order[0] < min_val:
            min_idx = idx
            min_val = order[0]

    if min_idx == -1:
        break

    # 1 2 3 5 4 6 9 7 4 10
    if solved[min_val]: continue
    solved[min_val] = 1

    print(orders[min_idx].pop(0), end=" ")
