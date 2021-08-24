import sys
from pandas import DataFrame
sys.stdin = open("input.txt", "r")


def run(i, j, f):
    # 현재 위치 x
    x = ls[i][j]
    # 현재 위치와 연속된 높이가 몇 개 있는지
    c = 1

    for k in range(1, n):
        # 다음 위치 y
        # 정방향
        if f == 0:
            y = ls[i][j + k]
        # 회전방향
        else:
            y = ls[i + k][j]

        # -------------------------------------------------------
        # 단차가 2 이상이면 X
        if abs(y - x) >= 2:
            return 0

        # 다음 위치 값이 더 높으면
        if x < y:
            # c가 l 이상이면 경사로를 놓을 수 있다.
            if c >= l:
                # 이후 다음 높이가 새로운 높이니까 c = 1로 초기화
                c = 1
            # 경사로를 놓지 못 함
            else:
                return 0

        # 다음 위치 값이 더 낮으면
        elif x > y:
            if c < 0:
                return 0
            # 다음이 낮으면, 현재 위치 앞으로 l개 만큼 경사로가 필요하니, 미리 땡겨쓴다.
            # 근데 바로 다음(y)가 있으니까 c = -l+1 로 초기화한다.
            # 이후 연속해서 다음 위치값과 현재 위치 값이 같은 경우(else쪽)에 속해야만 ok
            # 만약 if x<y 나 elif x>y에 걸리게 되면 c가 음수라 return 0이 된다.
            c = -l + 1

        # 다음 위치 값과 현재 위치 값이 같으면
        else:
            c += 1

        # 현재 위치 값에 다음 위치 값을 넣는다
        x = y
    # ----------------------------------------------------------
    # c가 음수면 X
    if c < 0:
        return 0

    return 1


n, l = map(int, input().split())
ls = [list(map(int, input().split())) for _ in range(n)]

row = [(i, 0) for i in range(n)]
col = [(0, i) for i in range(n)]
ans = 0
for i, j in row:
    ans += run(i, j, 0)
for i, j in col:
    ans += run(i, j, 1)
print(ans)