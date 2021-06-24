def solve(before: list):

    order.append(before)
    if len(state[3]) == N:
        return

    from_, to_ = before

    for i in range(1, 4):
        if len(state[i]):
            for j in range(1, 4):
                if i == j or (to_ == i and from_ == j) : continue
                if state[j] and state[j][-1] > state[i][-1]:
                    state[j].append(state[i].pop())
                    return solve([i, j])
                elif state[j] == []:
                    state[j].append(state[i].pop())
                    return solve([i, j])


N = int(input())
cnt = 0
order = []
state = [[], [i for i in range(N, 0, -1)], [], []]
solve([0, 0])
print(order)