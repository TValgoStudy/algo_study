import sys
sys.stdin = open('input.txt')

def appending(dictionary, key, value):
    if key not in dictionary or dictionary[key] >= value:
        dictionary[key] = value


def main():
    N, M = map(int, sys.stdin.readline().strip().split())
    mem = list(map(int, sys.stdin.readline().strip().split()))
    cost = list(map(int, sys.stdin.readline().strip().split()))

    minv = 1000000000

    DP = []

    for i in range(1, N + 1):
        nxt = {}
        tmpminv = 1000000000

        if mem[i - 1] >= M:
            minv = min(minv, cost[i - 1])
        else:
            appending(nxt, mem[i - 1], cost[i - 1])

        for j in DP:
            curM, curC = j

            if curC >= tmpminv:
                continue

            tmpminv = curC
            appending(nxt, curM, curC)

            nextM = curM + mem[i - 1]
            nextC = curC + cost[i - 1]

            if nextM >= M:
                minv = min(minv, nextC)
            else:
                appending(nxt, nextM, nextC)

        DP = [(i, nxt[i]) for i in nxt]
        DP.sort(reverse=True)

    print(minv)


if __name__ == '__main__':
    main()