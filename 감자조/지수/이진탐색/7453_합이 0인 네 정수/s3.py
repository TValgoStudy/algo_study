import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N = int(input())
A, B, C, D = [], [], [], []
answer = 0

for _ in range(N):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

total = {}
for a in A:
    for b in B:
        total[a+b] = total.get(a+b, 0) + 1

for c in C:
    for d in D:
        answer += total.get(-(c+d), 0)

print(answer)