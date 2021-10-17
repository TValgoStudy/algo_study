import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame


def calc():
    same_list = set()

    # 원판에 수가 남아 있으면, 인접하면서 수가 같은 것을 모두 찾는다
    for r in range(N):
        for c in range(-1, M-1):
            # 0이면 패스
            if not IN[r][c]:
                continue

            # 양쪽으로 같은 수가 있을 때
            if IN[r][c] == IN[r][c+1]:
                same_list.add((r, c))
                same_list.add((r, c+1))

            # 위 아래로 같은 수가 있을 때
            if r+1 < N and IN[r][c] == IN[r+1][c]:
                same_list.add((r, c))
                same_list.add((r+1, c))

    # 쌓아 둔 인접하면서 같은 수를 0으로 바꾼다.
    if same_list:
        for r, c in same_list:
            IN[r][c] = 0

    # 인접하면서 같은 수가 없을 때
    else:
        total = 0
        cnt = 0
        for r in range(N):
            total += sum(IN[r])
            cnt += (len(IN[r]) - IN[r].count(0))
        # cnt가 0이면 = 원판에 숫자가 없으면 return => zerodevision 방지
        if not cnt:
            return
        # 평균 계산해서 평균보다 크면 -1, 작으면 +1
        avg = total / cnt
        for r in range(N):
            for c in range(M):
                if not IN[r][c]:
                    continue
                if IN[r][c] > avg:
                    IN[r][c] -= 1
                elif IN[r][c] < avg:
                    IN[r][c] += 1


N, M, T = map(int, input().split())
IN = [list(map(int, input().split())) for _ in range(N)]

# d가 0 이면 시계 방향 => 맨 뒤에서 pop 해서 맨 앞에 넣기
# d가 1 이면 반시계 방향 => 맨 앞에서 pop해서 맨 뒤에 넣기
for _ in range(T):
    x, d, k = map(int, input().split())
    # x 배수인 원판 회전
    for r in range(x-1, N, x):
        # 반시계
        if d:
            IN[r] = IN[r][k:] + IN[r][:k]
        # 시계
        else:
            IN[r] = IN[r][-k:] + IN[r][:-k]
    calc()

result = 0
for r in range(N):
    result += sum(IN[r])
print(result)
