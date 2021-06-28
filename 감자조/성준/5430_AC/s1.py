import sys
sys.stdin = open('input.txt')


def ac(defs, N, strs):
    if N == 0:
        return 'error'
    else:
        nums = list(map(int, strs[1: N + N].split(',')))
        for d in defs:
            if d == 'R':
                nums.reverse()
            elif d == 'D':
                if len(nums) == 0:
                    return 'error'
                else:
                    nums.pop(0)
        return nums

T = int(input())

for _ in range(T):
    defs = list(input())
    N = int(input())
    strs = input()
    # print(defs)
    print(defs.count('R'))
    # print(ac(defs, N, strs))
