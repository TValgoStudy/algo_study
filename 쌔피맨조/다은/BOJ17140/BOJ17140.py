import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame


# dict가 빠른가 list가 빠른가?
def calc(matrix):
    M = len(matrix)
    fill_zero = 3
    for m in range(M):
        # 한 줄에 숫자 n이 몇 개 나왔는지 세는 dict
        num_dict = {}
        for num in matrix[m]:
            if num == 0:
                continue
            num_dict[num] = num_dict.get(num, 0) + 1

        # 해당 dict로 tmp_list만들어서 우선 정렬
        tmp_list = [(key, value) for key, value in num_dict.items()]
        tmp_list.sort(key=lambda x: (x[1], x[0]))

        # 정렬 수행한 걸로 바꿔치기
        matrix[m] = []
        for k, v in tmp_list:
            if len(matrix[m]) >= 100:
                break
            matrix[m].append(k)
            matrix[m].append(v)

        # 0으로 채워야 하는 max 길이 구하기
        if len(matrix[m]) > fill_zero:
            fill_zero = len(matrix[m])

    for m in range(M):
        fill_zero_list = [0] * (fill_zero - len(matrix[m]))
        matrix[m].extend(fill_zero_list)

    return matrix


r, c, k = map(int, input().split())
IN = [list(map(int, input().split())) for _ in range(3)]

r -= 1
c -= 1
time = 0
while time <= 100:
    # 이 부분을 체크 안해서 틀렸다. => 런타임 에러
    try:
        if IN[r][c] == k:
            break
    except:
        pass

    row_num, col_num = len(IN), len(IN[0])

    # R 연산 : 행 개수 >= 열 개수
    if row_num >= col_num:
        calc(IN)
    # C 연산 : 행 개수 < 열 개수
    else:
        IN_trans = calc([i for i in zip(*IN)])
        IN = [list(i) for i in zip(*IN_trans)]
    time += 1

# time이 100까지는 포함해야 함 => 안하면 75%에서 틀림
if time > 100:
    time = -1
print(time)
