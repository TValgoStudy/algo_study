import sys
sys.stdin = open('eval_input.txt')
# input = sys.stdin.readline

for _ in range(int(input())):
    funcs = input()
    n = int(input())
    nums = input().replace('[', '').replace(']', '').split(',')
    isreverse = False
    for func in funcs:
        if n == 0:
            print('error')
            break
        if func == 'R':
            isreverse = not isreverse
        else:
            if nums:
                if isreverse:
                    nums.pop()
                else:
                    nums.pop(0)
            else:
                print('error')
                break
    else:
        if isreverse:
            print('[' + ','.join(nums[::-1]) + ']')
        else:
            print('['+','.join(nums)+']')