import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame

from itertools import combinations

# 궁수가 죽일 타겟 위치(target)구하기 + 궁수와의 거리 dist
def attack(archer, IN_copy):
    target = (0, 0)
    dist = 9999999
    r1, c1 = archer

    for r2 in range(N):
        for c2 in range(M):
            if IN_copy[r2][c2] == 0:
                continue

            # 거리 구하기
            tmp = abs(r1-r2) + abs(c1-c2)

            # 킵해둔 dist보다 더 작은 타겟을 발견하면 갱신
            if tmp < dist and tmp <= D:
                dist = tmp
                target = (r2, c2)
            # 킵해둔 dist와 거리가 가깝고, 더 왼쪽인 타겟이면 갱신
            elif tmp == dist and tmp <= D:
                if target[1] > c2:
                    target = (r2, c2)

    return target if dist != 9999999 else (-1, -1)

def func(archer_index, IN_copy):
    # result: 죽인 적군의 수
    # cnt: 모든 적군의 수
    result = 0
    cnt = 0

    # 궁수 세명
    archer1 = (CASTLE, archer_index[0])
    archer2 = (CASTLE, archer_index[1])
    archer3 = (CASTLE, archer_index[2])

    # target_cnt(모든 적군 수)가 cnt(성 도달 + 궁수가 킬)와 같을 때까지 반복
    while target_cnt != cnt:

        # 궁수가 죽일 타겟 세명 위치
        target1 = attack(archer1, IN_copy)
        target2 = attack(archer2, IN_copy)
        target3 = attack(archer3, IN_copy)

        # 중복 위치 제외
        targets = set()
        if target1 != (-1, -1): targets.add(target1)
        if target2 != (-1, -1): targets.add(target2)
        if target3 != (-1, -1): targets.add(target3)
        # 적군 죽였은니 result, cnt +1
        for r, c in targets:
            IN_copy[r][c] = 0
            result += 1
            cnt += 1

        # 한 칸 내려와서 성에 도달 = IN_pop
        IN_pop = IN_copy.pop()
        # cnt에 더해 줌
        cnt += sum(IN_pop)
        # 앞에 한 줄 다시 채워 줌
        IN_copy.insert(0, [0]*M)
    return result



N, M, D = map(int, input().split())
IN = [list(map(int, input().split())) for _ in range(N)]

# 모든 적군의 수 구하기
target_cnt = 0
for r in range(N):
    for c in range(M):
        target_cnt += IN[r][c]

CASTLE = N
result = 0
# archer_index : 궁수 3명의 col 위치
for archer_index in combinations(range(M), 3):
    IN_copy = [i[:] for i in IN]
    result_tmp = func(archer_index, IN_copy)
    # 적의 최대수 갱신
    if result < result_tmp:
        result = result_tmp
print(result)