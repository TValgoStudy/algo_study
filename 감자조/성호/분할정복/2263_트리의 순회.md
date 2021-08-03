# 2263_트리의 순회



## 내 풀이(완전이진트리, 실패)

```python
import sys
sys.stdin = open('input.txt')

# 중위순회와 후위순회가 주어졌을 때 전위순회를 구해라?
# 후위순회의 마지막은 루트, 중위순회에서 그 루트를 찾아보면 양옆이 왼쪽, 오른쪽
# 왼쪽의 중심(/2)이 또 서브트리의 루트, 오른쪽의 중심이 또 서브트리의 루트, ...
N = int(input())
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))
order = []
root = post_order[-1]
order.append(root)
root_idx = in_order.index(root)
def find_order(in_order, root_idx):
    if len(in_order) == 1:
        return
      # 중위순회에서 root의 위치
    left_sub = in_order[:root_idx]
    left_root = len(left_sub) // 2
    order.append(left_sub[left_root])
    find_order(left_sub, left_root)
    if root_idx+1 >= len(in_order):
        return
    else:
        right_sub = in_order[root_idx+1:]
        right_root = len(right_sub) // 2
        order.append(right_sub[right_root])
        find_order(right_sub, right_root)

find_order(in_order, root_idx)
print(*order)
```

우선 후위순회로부터 root를 찾은 후 그걸 중위순회에서 찾으면 양옆이 서브트리이고, 그 중심이 다시 루트가 됨을 이용하여 이진탐색처럼 찾으려고 하였다.

그러나 이 방법은 완전이진트리에만 적용이 가능했다. 다른 사람의 풀이를 찾아보니 다음과 같았다.



## 다른 사람 풀이

```python
import sys
sys.stdin = open("input.txt")
sys.setrecursionlimit(10 ** 6)


def find_solution(l_in, r_in, l_post, r_post):

    if l_in > r_in or l_post > r_post:
        return

    parent = post_order[r_post]
    print(parent, end = " ")

    S_idx = idx[parent]
    left = S_idx - l_in

    find_solution(l_in, S_idx - 1, l_post, (l_post + left) - 1)
    find_solution(S_idx + 1, r_in, l_post + left, r_post - 1)


N = int(input())
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))

idx = [0] * (N+1)
for i in range(N):
    idx[in_order[i]] = i # in_order 원소의 인덱스 구하기

find_solution(0, N - 1, 0, N - 1)
```

나는 맨 처음에 root 노드를 구할 때만 post order를 사용하였는데, 그렇게 하면 안되고 매번 post order까지 잘라서 새로운 root를 찾아줘야 하는 것 같다.