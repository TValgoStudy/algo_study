N = int(input())
nums = list(map(int, input().split()))
# 덧셈(+)의 개수, 뺄셈(-)의 개수, 곱셈(×)의 개수, 나눗셈(÷)의 개수이다.
operators = list(map(int, input().split()))
operator_dict = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y, '/': lambda x, y: x // y}
# (n-1)!/a!b!c!d!
from itertools import product, permutations
max_ = - 100**11
min_ = 100**11

arr_operator = list('+'*operators[0] + '-'*operators[1] + '*'*operators[2] + '/'*operators[3])
for i in permutations(arr_operator):
    tmp = 0
    for idx, operator in enumerate(i):
        if idx == 0:
            tmp = operator_dict[operator](nums[idx], nums[idx+1])
        else:
            if operator == '/' and tmp < 0:
                tmp = -1 * operator_dict[operator](abs(tmp), nums[idx+1])
            else:
                tmp = operator_dict[operator](tmp, nums[idx+1])
    if tmp > max_:
        max_ = tmp
    if tmp < min_:
        min_ = tmp
# for j in product(arr_operator, repeat=2):
#     print(j)
print(max_, min_, sep='\n')