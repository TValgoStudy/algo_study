import sys
sys.stdin = open('input.txt')

def ac(defs, strs):
    flag = 1
    nums = list(strs[1: N + N].split(','))
    for d in defs:
        if d == 'R':
            flag *= -1
        # D인 경우
        else:
            # num가 비어있으면 error
            if len(nums) == 0:
                return 'error'
            if flag == 1:
                nums.pop(0)
            else:
                nums.pop()
    if len(nums) == 0:
        return '[]'
    if flag == -1:
        nums.reverse()
    return '[' + ','.join(nums) + ']'

T = int(input())
for _ in range(T):
    defs = list(input())
    N = int(input())
    strs = input()
    if N == 0:
        if defs.count('D'):
            print('error')
        else:
            print('[]')
    else:
        print(ac(defs, strs))
