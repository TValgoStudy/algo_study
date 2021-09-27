import sys
from pandas import DataFrame
sys.stdin = open("input.txt", "r")

from itertools import product
from collections import defaultdict

move = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


# 나무 번식
def spread_tree(tree, N, i, j, count):
    for a, b in move:
        newI = i + a
        newJ = j + b
        if (0 <= newI < N) and (0 <= newJ < N):
            tree[newI][newJ][1] += count


N, M, K = list(map(int, input().split()))
feed = [[] for _ in range(N)]
land = [[5 for _ in range(N)] for _ in range(N)]
tree = [[defaultdict(lambda: 0) for _ in range(N)] for _ in range(N)]

for i in range(N):
    feed[i] = list(map(int, input().split()))
for i in range(M):
    y, x, t = list(map(int, input().split()))
    tree[y - 1][x - 1][t] += 1


# 봄 : 나이만큼 양분 먹고 +1
def spring_summer_came(land, tree, N):
    for i, j in product(range(N), range(N)):
        update = defaultdict(lambda: 0)
        energy = 0
        # tree[i][j] : (i,j)에 있는 나무들 딕셔너리. 나이는 키, 개수는 벨류
        for t, num in sorted(tree[i][j].items()):
            # 양분 공급 나무 = min( 해당 양분//나이t ,나이t인 나무의 개수)
            # => 해당 양분//나이t : 해당 양분으로 나이t인 나무 몇개를 살릴 수 있는지
            alive = min(land[i][j] // t, num)
            dead = num - alive
            # 양분 공급 나무가 있으면 양분 재설정, 나무 나이도 재설정
            if alive > 0:
                land[i][j] -= t * alive
                update[t + 1] = alive
            # 죽은 나무는 양분으로 공급
            energy += (t // 2) * dead

        tree[i][j] = update
        land[i][j] += energy


# 가을 : 나이가 5의 배수인 나무는 번식
def fall_came(tree, N):
    for i, j in product(range(N), range(N)):
        for t, count in tree[i][j].items():
            # 나무 나이(키)가 5의 배수이고, 개수(벨류)가 0이 아니면 번식
            if (t % 5 == 0) and (count != 0):
                spread_tree(tree, N, i, j, count)


# 겨울 : 양분 공급
def winter_came(land, feed, N):
    for i, j in product(range(N), range(N)):
        land[i][j] += feed[i][j]


while K:
    spring_summer_came(land, tree, N)
    fall_came(tree, N)
    winter_came(land, feed, N)
    K = K - 1

treeN = 0
for i, j in product(range(N), range(N)):
    for t, num in tree[i][j].items():
        treeN += num

print(treeN)
