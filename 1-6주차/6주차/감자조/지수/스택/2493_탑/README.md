### 내 풀이

1. 이렇게 푼 이유?

   - 처음엔 이중반복문으로 현재 인덱스에서 왼쪽을 쭉 보는 방식으로 해서 시간초과
     - 아마 시간복잡도 n^2 ? nlogn? 이었던것 같다
   - DP!
     - DP를 써서 탐색의 반복수를 줄여서 통과
     - 왼쪽의 나보다 큰 탑중 가장 가까운 인덱스
     - 현재 탑보다 큰게 나올때 까지 DP로 껑충껑충 뛰면서 탐색

2. 실행시간

   - 528ms (python)

3. 코드

   ```python
   import sys
   sys.stdin = open('input.txt')
   
   # DP! 528ms
   
   N = int(input())
   tops = list(map(int, input().split()))
   tops = [0] + tops
   
   dp = [0] * (N+1) # dp[i] : i번째 탑보다 왼쪽에 있는것 중에 가장 가까운 큰 탑 번호
   
   
   for j in range(1, N+1):
       if tops[j] < tops[j-1]:
           dp[j] = j-1
       else:
           pre_top = dp[j-1]
           while tops[j] > tops[pre_top] and pre_top:
               pre_top = dp[pre_top]
           dp[j] = pre_top
   
   print(*dp[1:])
   ```



### 다른 사람의 풀이

1. 실행시간

   - 464ms

2. 코드

   ```python
   import sys
   
   def deep(index, num):
       if index == 0:
           return 0
   
       if nums[index] >= num: # 왼쪽 탑이 나보다 크면
           return index # 그 인덱스 선택
       else: # 그렇지 않으면 왼쪽탑보다 처음으로 큰 탑이 나오는 탑과 비교
           return deep(result[index], num)
   
   
   N = int(sys.stdin.readline())+1
   nums = list(map(int, sys.stdin.readline().split()))
   nums.insert(0, 0)
   
   # print(nums)
   
   result = [0] * N
   
   for i in range(2, N):
       if nums[i-1] > nums[i]:
           result[i] = i-1
       else:
           result[i] = deep(result[i-1], nums[i])
   
   
   print(' '.join(map(str, result[1:])))
   ```

3. 해설

   - deep을 구하는 부분이 내가 푼 풀이랑 비슷
   - 나는 while로, 여기는 재귀로