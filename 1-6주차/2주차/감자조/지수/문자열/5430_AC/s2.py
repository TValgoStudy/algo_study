import sys
sys.stdin = open('input.txt')
# input = sys.stdin.readline

def AC(funcs, n, nums):
    s, e = 0, n - 1
    isreverse = False

    if n == 0:
        if 'D' in funcs:
            return 'error'
        else:
            return [] # 함정..

    for func in funcs:
        if s >= n or e < 0:
            return 'error'

        if func == 'R':
            isreverse = not isreverse
            s, e = e, s
        else:
            if nums:
                if isreverse:
                    s -= 1
                else:
                    s += 1
            else:
                return 'error'

    if isreverse:
        return '[' + ','.join(nums[e:s + 1][::-1]) + ']'
    else:
        return '[' + ','.join(nums[s:e + 1]) + ']'


for _ in range(int(input())):
    funcs = input()
    n = int(input())
    nums = input().replace('[', '').replace(']', '').split(',')
    print(AC(funcs, n, nums))