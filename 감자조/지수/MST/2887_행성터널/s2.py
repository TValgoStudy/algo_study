import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# MST 구하는 방법 : 크루스칼(Union-find), 프림(힙)
# 1532 ms


def union(v, w):
    p_v = find(v)
    p_w = find(w)

    if p_v == p_w:
        return False

    if p_v < p_w:
        p[p_w] = p_v
    else:
        p[p_v] = p_w

    return True


def find(v):
    if v == p[v]:
        return v
    p[v] = find(p[v])
    return p[v]


N = int(input())
planet = [list(map(int, input().split())) + [idx] for idx in range(N)]

nodes = []

for i in range(3):
    planet.sort(key = lambda x: x[i])
    for j in range(N-1):
        nodes.append((abs(planet[j][i] - planet[j+1][i]), planet[j][3], planet[j+1][3]))

nodes.sort()

p = [i for i in range(N)]

connect = 0
MIN = 0

for d, v, w in nodes:
    if union(v, w):
        MIN += d
        connect += 1
    if connect == N-1:
        break

print(MIN)
