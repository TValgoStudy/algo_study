import sys
from pandas import DataFrame
sys.stdin = open("input.txt", "r")


def func(IN):
    result_tmp = 0
    check = [[0]*N for _ in range(N)]

    for r in range(N):
        flag = 0
        c = 0

        while c <= N-2:
            step = IN[r][c] - IN[r][c+1]

            # 단차가 1초과, -1미만이면 해당 row X
            if abs(step) > 1:
                flag = 1

            # 단차가 0이면 그냥 통과
            elif step == 0:
                c += 1

            # 단차가 1이면 [r][c+1]이 낮음
            elif step == 1:
                low_h = IN[r][c+1]
                # 경사로 L 놓을 자리 없으면 가망 X
                if c+L >= N:
                    flag = 1
                else:
                    # c+1 ~ c+L 까지 경사로 확인
                    for l in range(c+1, c+1+L):
                        # 경사로 있으면 X
                        if check[r][l]:
                            flag = 1
                            break
                        else:
                            # 경사로 만들기 (만들다 실패하면 그 row는 버릴거라 초기화 안해도 됨)
                            check[r][l] = 1

                        # 다 같은 높이여야 함
                        if low_h != IN[r][l]:
                            flag = 1
                            break
                    # break 안걸리고 정상적으로 끝나면 c+L로
                    else:
                        c += L

            # 단차가 -1이면 [r][c]가 낮음
            elif step == -1:
                low_h = IN[r][c]
                # 경사로 L 놓을 자리 없으면 가망 X
                if c-L+1 < 0:
                    flag = 1
                else:
                    # c ~ c-L+1 까지 경사로 확인
                    for l in range(c, c-L, -1):
                        # 경사로 있으면 X
                        if check[r][l]:
                            flag = 1
                            break
                        else:
                            # 경사로 만들기 (만들다 실패하면 그 row는 버릴거라 초기화 안해도 됨)
                            check[r][l] = 1
                        # 다 같은 높이여야 함
                        if low_h != IN[r][l]:
                            flag = 1
                            break
                    # break 안걸리고 정상적으로 끝나면 c+1로
                    else:
                        c += 1

            # 탈출 조건(flag=1) 만족하면 break
            if flag == 1:
                break

        # break에 안 걸리고 정상적으로 while이 끝났으면 경로+1
        else:
            # print(r)
            result_tmp += 1

    return result_tmp


N, L = map(int, input().split())
IN = [list(map(int, input().split())) for _ in range(N)]
IN_trans = [list(i) for i in zip(*IN)]

result = 0
result += func(IN)
result += func(IN_trans)
print(result)