### 내 풀이

1. 처음 풀이

   - 문제 그대로 풀었더니 시간초과

   ```python
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
       print(defs.count('R'))
   ```

2. 다시 푼 풀이

   - 시간을 줄이기 위해서 reverse대신 flag사용
   - 사전에 에러가 나는지 검사

   ```python
   T = int(input())
   
   def ac(strs, nums):
       # 에러상황
       if N < strs.count('D'):
           return 'error'
       else:
           # flag로 뒤집어진 상태를 확인
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
   ```

   - 결과는 틀림... 왜 틀렸을까...

