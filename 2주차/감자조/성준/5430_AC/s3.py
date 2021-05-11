import sys
sys.stdin = open('input.txt')

T = int(input())

def ac(strs, nums):
    # 에러상황
    if N < strs.count('D'):
        return 'error'
    else:
        flag = 1
        for s in strs:
            # s가 R이면 빼는 순서를 뒤집는다.
            if s == 'R':
                flag *= -1
            # s가 D이면 flag에 맞는 원소를 지운다.
            if s == 'D':
                if flag == 1:
                    nums.pop(0)
                else:
                    nums.pop()
        if flag == 1:
            return '[' + ','.join(nums) + ']'
        else:
            nums.reverse()
            return '[' + ','.join(nums) + ']'

for _ in range(T):
    strs = list(input())
    N = int(input())
    nums = input()[1:N+N].split(',')
    print(ac(strs, nums))