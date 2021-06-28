import sys
sys.stdin = open('input.txt')

N = int(input())
p = [i for i in range(N+1)]

for _ in range(N-1):
    v, w = map(int, input().split())
    if v > w:
        v, w = w, v
    p[w] = v

def findCommonParent(x, y):
    while x != y:
        if x > y:
            x = p[x]
        else:
            y = p[y]
    return x

M = int(input())
for _ in range(M):
    x, y = map(int, input().split())
    print(findCommonParent(x, y))

