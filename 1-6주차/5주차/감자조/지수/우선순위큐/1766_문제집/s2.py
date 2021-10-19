import sys
sys.stdin = open('input.txt')
q = lambda : map(int, sys.stdin.readline().split())

# 먼저 푸는 것, 쉬운 문제 -> 우선순위
# 우선순위 큐 = 힙?
# 먼저 푸는게 바로 다음에 푼다는 뜻인듯? 바로 다음에 푸는게 아니라면 3-1-4-2도 되야함
# 서로소집합을 만들어서 부모 저장 서로 다른 그룹중에서는 root가 작은 그룹 먼저 풀기

N, M = q()

# 부모(먼저풀문제), 자식(다음에풀문제)
pc = [[i, []] for i in range(N+1)]
orders = []

def setPC(A, B):
    pc[B][0] = A
    pc[A][1].append(B)

def findOrder(problem):
    temp = [problem]

    que = pc[problem][1]
    while que:
        child = que.pop(0)
        temp.append(child)
        que.extend(pc[child][1])

    orders.append(temp)

def findRoot():
    for j in range(1, N+1):
        if j == pc[j][0]: # 자기자신이 부모이면 root
            findOrder(j)

for _ in range(M):
    A, B = q()
    setPC(A, B)

findRoot()

orders.sort()

for order in orders:
    print(*order, end=" ")