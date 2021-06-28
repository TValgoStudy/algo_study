import sys
sys.stdin = open('input.txt')

N = int(input())
p = [i for i in range(N+1)]
DP = {}

for _ in range(N-1):
    v, w = map(int, input().split())
    if v > w:
        v, w = w, v
    p[w] = v

def findCommonParent(x, y):
    c_x, c_y = x, y

    while x != y:
        if DP.get((x, y), 0):
            return DP[(x, y)]
        if x > y:
            x = p[x]
        else:
            y = p[y]

    DP[(c_x, c_y)] = x
    DP[(c_y, c_x)] = x
    return x

M = int(input())
for _ in range(M):
    x, y = map(int, input().split())
    print(findCommonParent(x, y))

