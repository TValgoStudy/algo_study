import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**6)

n = int(input())
inOrder = list(map(int, input().split())) # 왼쪽 -> 부모 -> 오른쪽
postOrder = list(map(int, input().split())) # 왼쪽 -> 오른쪽 -> 부모

tree = [0] * (n+1)

for i in range(n):
    tree[inOrder[i]] = i

def devide(in_start, in_end, post_start, post_end):

    if in_start > in_end or post_start > post_end:
        return

    parents = postOrder[post_end]
    print(parents, end=" ")

    left = tree[parents] - in_start
    right = in_end - tree[parents]

    devide(in_start, in_start + left -1, post_start, post_start + left - 1)
    devide(in_end - right + 1, in_end, post_end - right, post_end - 1)


devide(0, n-1, 0, n-1)

