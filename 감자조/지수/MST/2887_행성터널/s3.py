import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def find(target):
    if disjointSet[target] == target:
        return target

    disjointSet[target] = find(disjointSet[target])
    return disjointSet[target]


def union(sv, dv):
    findSV = find(sv)
    findDV = find(dv)

    if findSV == findDV:
        return False

    if findSV < findDV:
        disjointSet[findDV] = findSV
    else:
        disjointSet[findSV] = findDV

    return True


def kruskal():
    global ans

    for w, sv, dv in tunnel:
        if union(sv, dv):
            ans += w


N = int(input())

ans = 0
disjointSet = [x for x in range(N)]

coords = [list(map(int, input().split())) + [x] for x in range(N)]

tunnel = []

coords.sort()
for i in range(N - 1):
    tunnel.append((abs(coords[i][0] - coords[i + 1][0]), coords[i][3], coords[i + 1][3]))
coords.sort(key=lambda x: x[1])
for i in range(N - 1):
    tunnel.append((abs(coords[i][1] - coords[i + 1][1]), coords[i][3], coords[i + 1][3]))
coords.sort(key=lambda x: x[2])
for i in range(N - 1):
    tunnel.append((abs(coords[i][2] - coords[i + 1][2]), coords[i][3], coords[i + 1][3]))

tunnel.sort()

kruskal()

print(ans)
print(disjointSet)