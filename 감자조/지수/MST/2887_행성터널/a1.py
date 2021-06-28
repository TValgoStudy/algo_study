import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def find_dist(coord, edge, n, k):
    coord.sort(key=lambda x: x[k])
    for i in range(n - 1):
        edge.append((abs(coord[i][k] - coord[i + 1][k]), coord[i][3], coord[i + 1][3]))


def solution():
    input = sys.stdin.readline
    INF = float("inf")
    n = int(input())
    parent = [i for i in range(n + 1)]
    coord = []
    edge = []
    result = 0

    for i in range(1, n + 1):
        x, y, z = map(int, input().split())
        coord.append((x, y, z, i))

    find_dist(coord, edge, n, 0)
    find_dist(coord, edge, n, 1)
    find_dist(coord, edge, n, 2)

    edge.sort()

    for cost, a, b in edge:
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result += cost

    print(result)


solution()