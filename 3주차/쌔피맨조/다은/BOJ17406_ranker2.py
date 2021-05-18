import sys

input = sys.stdin.readline
def rotate(arr, r, c, s):
    arr = [row[:] for row in arr]
    i = 1
    while i <= s and i <= r < N - i and i <= c < M - i:
        temp = arr[r-i][c-i]
        for y in range(r - i, r + i):
            arr[y][c-i] = arr[y+1][c-i]
        arr[r+i][c-i:c+i] = arr[r+i][c-i+1:c+i+1][:]
        for y in range(r + i, r - i, -1):
            arr[y][c+i] = arr[y-1][c+i]
        arr[r-i][c-i+1:c+i+1] = arr[r-i][c-i:c+i][:]
        arr[r-i][c-i+1] = temp
        i += 1
    return arr


def permutation(arr, k=0):
    global res
    if k == K:
        min_value = min([sum(row) for row in arr])
        if res > min_value:
            res = min_value
        return

    for i in range(K):
        if not vis[i]:
            r, c, s = ope[i]
            vis[i] = True
            temp = rotate(arr, r, c, s)
            permutation(temp, k+1)
            vis[i] = False


N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

ope = []
for i in range(K):
    r, c, s = map(int, input().split())
    r -= 1
    c -= 1
    ope.append((r, c, s))

vis = [False] * K
res = 987654321
permutation(arr)
print(res)