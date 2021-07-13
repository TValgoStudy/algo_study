import sys
sys.stdin = open("input2.txt", "r")

def calc(n1, op, n2):
    if op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2
    else:
        return n1 * n2

def solve(cur, cnt):
    global ans
    if cnt == N//2:
        ans = max(ans, cur)
        return

    # 괄호가 없이
    res = calc(cur, op1[cnt], op2[cnt+1])
    solve(res, cnt+1)
    # 괄호가 포함될 때
    if cnt <= N//2 - 2:
        next = calc(op2[cnt+1], op1[cnt+1], op2[cnt+2])
        res = calc(cur, op1[cnt], next)
        solve(res, cnt+2)

N = int(input())
k = input()
op1, op2 = [], []

for i in range(N):
    if i % 2:
        op1.append(k[i])
    else:
        op2.append(int(k[i]))

ans = -float('inf')
solve(op2[0], 0)
print(ans)