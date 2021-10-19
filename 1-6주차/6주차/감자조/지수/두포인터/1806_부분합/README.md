### 내 풀이

1. 이렇게 푼 이유?

   - 프로그래머스 보석쇼핑의 하위호환
   
2. 실행시간

   - 168ms (python)

3. 코드

   ```python
   import sys
   sys.stdin = open('input.txt')
   q = lambda : map(int, sys.stdin.readline().split())
   
   # 168ms
   # 포인터 s,e 사용
   # 구간합이 S보다 작으면 e + 1
   # 구간합이 S보다 크면 MIN 갱신, s + 1
   
   N, S = q()
   nums = list(q())
   
   s, e = 0, 0
   total = nums[0]
   
   MIN = 900000000
   
   while s < N:
   
       if total >= S:
           MIN = min(MIN, e-s+1)
   
       elif e < N-1:
           e += 1
           total += nums[e]
           continue
   
       total -= nums[s]
       s += 1
   
   if MIN == 900000000:
       print(0)
   else:
       print(MIN)
   ```



### 다른 사람의 풀이

1. 실행시간

   - 116ms

2. 코드

   ```python
   from sys import stdin
   
   input = stdin.readline
   
   def solve():
   
       N, S = map(int, input().split())
   
       arr = list(map(int, input().split()))
   
       inf = float('inf')
       left, sum_val, ans= 0, 0, inf
   
       for right in range(N):
           sum_val += arr[right] # 오른쪽  추가될때 마다 +
           while sum_val - arr[left] >= S: # 왼쪽 값 빼도 구간합이 타겟보다 크면
               sum_val -= arr[left] # 왼쪽값 빼기
               left += 1 # 구간 땡기기
   
           if sum_val >= S and ans > right - left: # 갱신 가능하면 갱신
               ans = right - left + 1
   
       print(ans if ans != inf else 0)
       return
   
   solve()
   ```
   
3. 해설

   - 내 풀이랑 비슷
   - 왼쪽을 빼도 되면 쭉 빼기
   - 오른쪽은 for문으로 무조건 한칸씩 넘어가게
   - while 조건이 왼쪽을 땡겨도 될때만 들어가게 해서 불필요한 연산을 줄여 빠른 것 같음