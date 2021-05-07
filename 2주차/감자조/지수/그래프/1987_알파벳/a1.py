import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# 다른 사람 풀이
R, C = map(int, input().split())
arr = [ list(input()) for _ in range(R) ]

result = 0
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

stack = [(0, 0, 1, arr[0][0])]
visit = [[''] * C for _ in range(R)]
visit[0][0] += arr[0][0]

while stack:
    r, c, dist, concate = stack.pop(0)

    if dist > result:
        result = dist
        
    if result == 26: # 알파벳 총 갯수
        break
        
    for k in range(4):
        nr, nc = r + dr[k], c + dc[k]
        if 0 <= nr < R and 0 <= nc < C:
            new_s = concate + arr[nr][nc]
            if visit[nr][nc] != new_s and arr[nr][nc] not in concate:
                visit[nr][nc] = new_s
                stack.append((nr, nc, dist+1, new_s))

print(result)

