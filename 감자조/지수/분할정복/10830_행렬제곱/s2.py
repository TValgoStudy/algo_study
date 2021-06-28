import sys
sys.stdin = open('eval_input.txt')
input = sys.stdin.readline

N, B = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
memo = {}
for i in range(N):
    for j in range(N):
        A[i][j] %= 1000
memo[1] = A

# 나누기
def divide(B):
    # 나온적 있는 결과면 계산 없이 바로 memo 리턴
    if memo.get(B, 0):
        return memo[B]
    else:
        if B%2 == 0: # 짝수면
            memo[B] = conquer(divide(B//2), divide(B//2))
        else:
            memo[B] = conquer(divide(B-1), A)
        return memo[B]

# 두 행렬의 곱
def conquer(A1, A2):
    C = [[0] * N for _ in range(N)]
    for i, row in enumerate(A1):
        for j, col in enumerate(zip(*A2)):
            C[i][j] = sum([r * c for r, c in zip(row, col)]) % 1000

    return C

result = divide(B)

for res in result:
    print(*res)
