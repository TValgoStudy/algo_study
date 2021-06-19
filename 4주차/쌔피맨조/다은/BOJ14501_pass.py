import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame

N = int(input())
IN = [[0, 0]] + [list(map(int, input().split())) for _ in range(N)]
IN = [list(i) for i in zip(*IN)]
BP = [0] * (N+2)

for i in range(1, N+1):
    # 상담 기간이 퇴사 전이면
    if i + IN[0][i] < N + 2:
        # 기존 BP 값보다 새로 갱신하는 값이 더 크면
        if BP[i+IN[0][i]] < BP[i] + IN[1][i]:
            # 그 이후 값들을 새로 갱신할 건데,
            for _ in range(i+IN[0][i], N+2):
                # 그 이후 값들 중에서 더 큰 값이 있으면 스루하고
                # 더 작은 값들만 갱신한다.
                if BP[_] < BP[i] + IN[1][i]:
                    BP[_] = BP[i] + IN[1][i]
print(max(BP))