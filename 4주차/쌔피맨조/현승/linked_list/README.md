# 연결 리스트

- 배열과 함께 가장 기본이 되는 대표적인 **선형** 자료구조
- 메모리를 물리적인 순서대로 저장하지 않아도 되기 때문에 관리가 쉽다.
- 동적으로 새로운 노드를 삽입, 삭제하기가 간편하다
- 단 중간에 있는 값을 배열 처럼 O(1)로 가져올 수 없다.





## 기본 연결리스트

기본적으로는 노드마다 next라는 속성을 통해 다음 노드를 가리키는 구조로 되어있다.

```python
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 노드의 값이 1 ~ 8 까지로 주어진다.
list1 = [1, 2, 3, 4, 5, 6, 7, 8]

# 처음 노드 생성
head = ListNode(list1[0])
node = head

# 노드 생성 및 연결해주기
for i in range(1, len(list1)):
    node.next = ListNode(list1[i])
    node = node.next
    
# 모든 노드 출력
node = head
while node.next != None:
    print(node.val)
    node = node.next
print('마지막 노드: ', node.val)

"""
1 2 3 4 5 6 7 마지막 노드:  8
"""
```



## 트리에서의 연결리스트

- 그냥 리스트로 구현했을 때와 거의 동일하게 구현이 가능하다.
- 기본 노드의 next  속성 대신 left, right, parent 속성이 각각 자식과 부모노드를 가리킨다.

- 하지만 문제 중에 종종 트리의 연결을 끊거나 연결하는 식으로 조작하는 문제들이 있는데 그 경우에 연결리스트로 트리를 구현해야 문제를 풀 수 있을 것 같다.

```python
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
print()

print('중위 순회 : ', end='')
in_order(nodes[1])
print()

print('후위 순회 : ', end='')
post_order(nodes[1])
print()


"""
전위 순회 : 1 2 4 7 12 3 5 8 9 6 10 11 13 
중위 순회 : 12 7 4 2 1 8 5 9 3 10 6 13 11 
후위 순회 : 12 7 4 2 8 9 5 10 13 11 6 3 1
"""
```



