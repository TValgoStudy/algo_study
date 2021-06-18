import sys
sys.stdin = open('input.txt')
q = lambda : map(int, sys.stdin.readline().split())

# 친구가 모두 얼리어답터여야 받아 들인다
# 친구는 부모 노드, 자식 노드들이다

# 자식이 중 하나라도 얼리어답터가 아니면 부모는 반드시 얼리어답터
# 자식이 모두 얼리어답터이면 부모는 얼리어답터여도 되고 아니여도 되고

N = int(input())

tree = [[] for _ in range(N+1)]
parent = [i for i in range(N+1)]
leaf = []
check = [0] * (N+1)

for _ in range(N-1):
    p, c = q()
    tree[p].append(c)
    parent[c] = p

for i in range(1, N+1):
    if not tree[i]:
        leaf.append(i)
        check[parent[i]] = 1


def isNotChildEarly(node):
    for child in tree[node]:
        if not check[child]:
            return True
    return False


while leaf:
    node = leaf.pop(0)

    if isNotChildEarly(node):
        check[node] = 1

        if node != parent[node]:
            leaf.append(parent[node])

    else: # 모든 자식이 얼리어답터
        if node != parent[node]:
            leaf.append(parent[node])


print(sum(check))



