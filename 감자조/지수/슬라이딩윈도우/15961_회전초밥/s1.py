import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

dishes, cnt, serial, coupon = map(int, input().split())
belt = []
ate = {}
ans = 1
MAX = 0

for _ in range(dishes):
    susi = int(input())
    belt.append(susi)
    ate[susi] = 0

ate[coupon] += 1 # 공짜로 주는 거

for i in range(dishes-serial+1):
    if i == 0:
        for k in range(serial):
            if ate[belt[k]] == 0: ans += 1 # 안먹어본 종류면 + 1
            ate[belt[k]] += 1
    else:
        if ate[belt[i - 1]] == 1: ans -= 1
        ate[belt[i - 1]] -= 1
        if ate[belt[i + serial - 1]] == 0: ans += 1
        ate[belt[i + serial - 1]] += 1

    MAX = max(MAX,ans)

print(MAX)

