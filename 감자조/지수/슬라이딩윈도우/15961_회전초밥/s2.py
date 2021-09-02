import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# 1160ms pypy

def solution():
    dishes, cnt, serial, coupon = map(int, input().split())
    belt = []
    ate = {}
    ans = 1
    result = 0

    for _ in range(dishes):
        susi = int(input())
        belt.append(susi)
        ate[susi] = 0

    ate[coupon] = 1  # 공짜로 주는 거

    for i in range(dishes):
        if i == 0:
            for k in range(serial):
                if ate[belt[k]] == 0: ans += 1 # 안먹어본 종류면 + 1
                ate[belt[k]] += 1
        else:
            if ate[belt[i - 1]] == 1: ans -= 1
            ate[belt[i - 1]] -= 1

            if ate[belt[(i + serial - 1) % dishes]] == 0: ans += 1
            ate[belt[(i + serial - 1) % dishes]] += 1

        result = max(result, ans)

        if result == serial + 1: # 먹을 수 있는 최대이면 바로 종료
            return result

    return result

print(solution())