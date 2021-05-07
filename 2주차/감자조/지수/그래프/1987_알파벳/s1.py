import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# 내 풀이
R, C = map(int, input().split())
arr = [ list(input()) for _ in range(R) ]

result = 0
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

visit = []

def DFS(r, c, s):
    global result

    for k in range(4):
        nr, nc = r + dr[k], c + dc[k]
        if 0 <= nr < R and 0 <= nc < C and arr[nr][nc] not in s:
            DFS(nr, nc, s+arr[nr][nc])

    if len(s) > result:
        result = len(s)

DFS(0, 0, arr[0][0])
print(result)



