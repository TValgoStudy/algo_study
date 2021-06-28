from sys import stdin
stdin = open('input.txt')

def sol12865():
    n, k, *items = map(int, stdin.read().split())
    dp = {0:0}
    for i in range(0, n * 2, 2):
        w, v = items[i], items[i+1]
        if v > 0 and w <= k:
            update = {}
            for key, value in dp.items():
                weight = key + w
                if weight <= k and value + v > dp.get(weight, 0):
                    update[weight] = value + v
            dp.update(update)
    print(max(dp.values()))


if __name__ == '__main__':
    sol12865()