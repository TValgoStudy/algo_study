def perm(idx):
    if idx == M:
        print(*sel)
    else:
        for i in range(N):
            if not check[i]:
                sel[idx] = numbers[i]
                check[i] = 1
                perm(idx + 1)
                check[i] = 0


N, M = map(int, input().split())
sel = [0] * M
check = [0] * N
numbers = [i for i in range(1, N + 1)]
perm(0)

