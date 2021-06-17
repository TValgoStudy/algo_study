def dfs(idx: int, total: int):
    global MAX, MIN

    if idx == N:
        MAX = max(MAX, total)
        MIN = min(MIN, total)
        return

    if operators[0]:
        operators[0] -= 1
        dfs(idx + 1, total + numbers[idx])
        operators[0] += 1

    if operators[1]:
        operators[1] -= 1
        dfs(idx + 1, total - numbers[idx])
        operators[1] += 1

    if operators[2]:
        operators[2] -= 1
        dfs(idx + 1, total * numbers[idx])
        operators[2] += 1

    if operators[3]:
        operators[3] -= 1
        dfs(idx + 1, int(total / numbers[idx]))
        operators[3] += 1


N = int(input())
numbers = list(map(int, input().split()))
MIN = 1000000000
MAX = -1000000000
operators = list(map(int, input().split()))
dfs(1, numbers[0])
print(MAX)
print(MIN)

