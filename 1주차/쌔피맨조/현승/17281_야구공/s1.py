import sys
sys.stdin = open("input.txt", "r")
import time
start = time.time()

# 완탐?
# 1이닝 8! * 9 = 40만
# 최대 50이닝 = 2000만
# 각 이닝이 독립적이지도 않다
# 가지치기? 9회 갈때까지 가지치기 할 수가 있나?
# 방법 모르겠음 그냥 완전탐색으로 하자

# 1회에 얻을 수 있는 최대점수 : 24점
# 현재 최고점수

from itertools import permutations
from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
# 이닝
turns = [list(map(int, input().split())) for _ in range(N)]
# 0 ~ 8번 타자 순서
orders = [1, 2, 3, 4, 5, 6, 7, 8]

max_score = 0

for perm in permutations(orders, 8):
    player_order = []
    for i, player_num in enumerate(perm):
        if i == 3:
            player_order.append(0)
        player_order.append(player_num)

    cur = 0
    out = 0
    ru = deque()
    score = 0
    for turn in turns:

        while out < 3:
            person_num = player_order[cur]
            # 아웃이면 아웃카운트1
            if turn[person_num] == 0:
                out += 1
            # 안타치면 모든 주자 한 루씩 진루
            elif turn[person_num] == 1:
                ru.appendleft(1)
            # 2루타
            elif turn[person_num] == 2:
                ru.appendleft(1)
                ru.appendleft(0)
            # 3루타
            elif turn[person_num] == 3:
                ru.appendleft(1)
                ru.appendleft(0)
                ru.appendleft(0)
            else:
                score += sum(ru) + 1
                ru = deque()

            if len(ru) > 3:
                while len(ru) > 3:
                    # 0이면 점수 변화 x, 1이면 점수 1
                    score += ru.pop()

            # 다음타자로
            cur += 1
            if cur >= 9:
                cur = 0
        # 해당 이닝이 끝나면 주자, 아웃 리셋
        ru = deque()
        out = 0

    if max_score < score:
        max_score = score

print(max_score)
print("time: ", time.time() - start)
