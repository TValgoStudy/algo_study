### 내 풀이

2. 실행시간
   - 2396ms

3. 코드

   ```python
   import sys
   sys.stdin = open('input.txt')
   input = sys.stdin.readline
   
   target = int(input())
   N = int(input())
   broken = list(map(int, input().split()))
   
   button = [1] * 10
   for b in broken:
       button[b] = 0
   
   
   MIN = abs(target - 100)
   
   for chanel in range(0, 1000001):
       for ch in str(chanel):
           if button[int(ch)] == 0:
               break
       else:
           MIN = min(MIN, len(str(chanel)) + abs(target - chanel))
   
   print(MIN)
   ```
   
3. 해석
   - 이렇게 무식한 방법일줄 몰랐는데 500000번도 생각보다 느리지 않음
   - 진짜 0~1000000번의 누를수 있는 번호 중에서 가장 이동거리가 최소인 것을 찾음



### 다른 사람의 풀이

1. 실행시간

   - 56ms

2. 코드

   ```python
   import sys
   sys.stdin = open('input.txt')
   
   N = int(input())
   broken = []
   if int(input()) != 0:
       broken = list(map(int, input().split()))
   available = [str(n) for n in range(10) if n not in broken]
   available.sort()
   maxDistance = abs(N - 100)
   maxDistanceList = [maxDistance]
   sN = str(N)
   if len(available) == 0:
       print(maxDistance)
       exit()
   if len(available) == 1 and available[0] == '0':
       maxDistanceList.append(N + 1)
       print(min(maxDistanceList))
       exit()
   
   
   def findBS(findString, startIndex, resultString):
       if len(findString) <= startIndex:
           return resultString
       for i in available:
           if int(findString[0:startIndex+1]) <= int(resultString + i):
               r = findBS(findString, startIndex + 1, resultString + i)
               if r:
                   return r
       if startIndex == 0:
           return findBS('0' + findString, startIndex, resultString)
       else:
           return None
   
   
   def findSB(findString, startIndex, resultString):
   
       if len(findString) <= startIndex:
           return resultString
   
       for i in reversed(available):
           if int(findString[0:startIndex+1]) >= int(resultString + i):
               r = findSB(findString, startIndex + 1, resultString + i)
               if r:
                   return r
   
       if startIndex == 0:
           return findSB(findString, startIndex + 1, resultString)
       else:
           return None
   
   
   bs = findBS(sN, 0, '')
   if bs:
       bs = str(int(bs))
       maxDistanceList.append(len(bs) + int(bs) - N)
   sb = findSB(sN, 0, '')
   if sb:
       sb = str(int(sb))
       maxDistanceList.append(len(sb) + N - int(sb))
   
   print(min(maxDistanceList))
   ```
   
3. 해설

   - `findBS` : 타겟보다 큰 수 중에서 가장 작은 누를 수 있는 수

   - `findSB` : 타겟보다 작은 수 중에서 가장 큰 누를 수 있는 수

   - 비교 연산으로 해결

   - 비슷하게 풀었지만 틀렸던 나의 풀이

     ```python
     target = input()
     B = int(input())
     
     broken = [0] * 10
     for n in list(map(int, input().split())):
         broken[n] = 1
     
     T = len(target)
     MIN = 987564321
     
     def pushButton(idx, num):
         global MIN
     
         if idx == T:
             MIN = min(MIN, abs(int(num) - int(target)))
             return
     
         if broken[int(target[idx])] == 0:
             pushButton(idx+1, num + target[idx])
         else:
             for i in range(1, 10):
                 x = int(target[idx]) + i
                 if x > 9: x = 0
                 if broken[x] == 0:
                     pushButton(idx + 1, num + str(x))
                     break
     
             for i in range(1, 10):
                 x = int(target[idx]) - i
                 if x < 0: x = 9
                 if broken[x] == 0:
                     pushButton(idx + 1, num + str(x))
                     break
     
     
     
     pushButton(0, '')
     
     print(min(MIN + T, abs(int(target) - 100)))
     ```

     

