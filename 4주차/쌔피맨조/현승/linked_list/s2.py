# 이진트리 연결리스트로 구현해보기
"""
V : 정점 개수, 1 ~13
E : 간선 개수, V-1
2개 단위로 부모 자식
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
"""
V = 13
E = 12
tmp = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6, 4, 7, 5, 8, 5, 9, 6, 10, 6, 11, 7, 12, 11, 13]

class Node:
    def __init__(self, x):
        self.val = x
        self.parent = x
        self.left = None
        self.right = None

# 전위 순회 (V -> L -> R)
def pre_order(node):

    if node == None:
        return

    print(node.val, end=' ')
    pre_order(node.left)
    pre_order(node.right)

# 중위 순회 (L -> V -> R)
def in_order(node):

    if node == None:
        return

    in_order(node.left)
    print(node.val, end=' ')
    in_order(node.right)

# 후위 순회 (L -> R -> V)
def post_order(node):

    if node == None:
        return

    post_order(node.left)
    post_order(node.right)
    print(node.val, end=' ')

# 1 ~ 13까지 node 인스턴스로 만들어서 nodes에 순서대로 저장하기
nodes = [None]
for i in range(1, 14):
    nodes.append(Node(i))

# 트리구조 만들기
for i in range(E):
    parent = tmp[2 * i]
    child = tmp[2 * i + 1]

    if not nodes[parent].left:
        nodes[parent].left = nodes[child]
    else:
        nodes[parent].right = nodes[child]

    nodes[child].parent = nodes[parent]

print('전위 순회 : ', end='')
pre_order(nodes[1])
# print(cnt)
print()

print('중위 순회 : ', end='')
in_order(nodes[1])
print()

print('후위 순회 : ', end='')
post_order(nodes[1])
print()