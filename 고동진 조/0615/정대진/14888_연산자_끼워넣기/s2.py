N = int(input())
nums = list(map(int, input().split()))
operators = list(map(int, input().split()))
max_ = - 100**11
min_ = -max_
operator_dict = {0: lambda x, y: x + y, 1: lambda x, y: x - y, 2: lambda x, y: x * y, 3: lambda x, y: x // y}


def backtracking(level=1, total=0):
    global operators, N, max_, min_, nums
    if level == N:
        if total > max_:
            max_ = total
        if total < min_:
            min_ = total
        return
    for idx in range(4):
        if operators[idx]:
            operators[idx] -= 1
            if level == 1:
                backtracking(level=level+1, total=operator_dict[idx](nums[0], nums[1]))
            else:
                if idx == 3 and total < 0:
                    next_total = -1 * operator_dict[idx](abs(total), nums[level])
                else:
                    next_total = operator_dict[idx](total, nums[level])
                backtracking(level=level+1, total=next_total)
            operators[idx] += 1


backtracking()
print(max_, min_, sep='\n')