import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame

# 156ms(pypy)
# 76ms(python)


def bfs(s, check, ab):
    q = [s]
    check[s] = 3
    people = IN[s]
    while q:
        v = q.pop(0)
        for w in G[v]:
            if check[w-1] == ab:
                check[w-1] = 3
                people += IN[w-1]
                q.append(w-1)
    return people, sum(check)

def my_func(idx, check):
    global result

    if idx == N:
        try:
            a = check.index(1)
            b = check.index(0)
            A_people, checksum1 = bfs(a, check[:], 1)
            B_people, checksum2 = bfs(b, check[:], 0)

            # 인접한 곳이 없을 때(check가 3이 안 될때) 에러검출
            if checksum1 + checksum2 == sum(check) + 3 * N:
                # 인구 차이의 최솟값으로 갱신
                tmp = abs(A_people - B_people)
                if tmp < result:
                    result = tmp
        except:
            pass
        return

    # 해당 선거구가 빨강(on)인지 파랑(off)인지
    check[idx] = 1
    my_func(idx+1, check)
    check[idx] = 0
    my_func(idx+1, check)



N = int(input())
IN = list(map(int, input().split()))

# on/off랑 visited 체크
check = [0] * N

# 1부터 시작하므로 인접행렬 연산할 때 -1 해주기
G = []
for _ in range(N):
    tmp = list(map(int, input().split()))
    G.append(tmp[1:])

result = 999999
my_func(0, check)
if result == 999999:
    result = -1
print(result)