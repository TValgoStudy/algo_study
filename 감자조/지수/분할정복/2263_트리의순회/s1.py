# 테케 10000까지로 늘려서 해봤는데 오류 없는데 문제에서는 인덱스 에러남
# pre order는 부모 -> 왼쪽 -> 오른쪽
# 포스트 오더에서는 맨뒤에 루트가 온다

import sys
sys.stdin = open('input.txt')

n = int(input())
inOrder = list(map(int, input().split())) # 왼쪽 -> 부모 -> 오른쪽
postOrder = list(map(int, input().split())) # 왼쪽 -> 오른쪽 -> 부모

tree = [0] * (n+1)

def devide(pivot_arr, target_arr, node):
    if len(pivot_arr) <= 1:
        if pivot_arr:
            tree[node] = pivot_arr[0]
        return

    tree[node] = pivot_arr[-1]
    pivot = target_arr.index(pivot_arr[-1])
    left = pivot_arr[:pivot]
    right = pivot_arr[pivot:-1]

    devide(left, target_arr[:pivot], node*2)
    devide(right, target_arr[pivot+1:], node*2+1)


devide(postOrder, inOrder, 1)

print(*tree[1:n+1])

# 12
# 8 4 9 2 10 5 11 1 12 6 3 7
# 8 9 4 10 11 5 2 12 6 7 3 1

