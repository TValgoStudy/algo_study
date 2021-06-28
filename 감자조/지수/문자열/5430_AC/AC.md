### 내 풀이

1. 이렇게 푼 이유?
   - 처음엔 R은 [::-1], D는 pop으로 했더니 시간초과
   - 파이썬에서 pop이나, 슬라이싱은 시간이 오래 소요되는 거라고 생각해서 인덱스로 접근
   - 시작, 끝 인덱스만 지정해두고 D가 나올때는 시작인덱스를 조정, R이 나오면 시작과 끝 인덱스를 스왑
   
2. 실행시간
   - 200ms

3. 코드

   ```python
   import sys
   sys.stdin = open(eval_input.txt)
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
   ```
   



### 다른 사람의 풀이

1. 실행시간

   - 180ms

2. 코드

   ```python
   import sys
   sys.stdin = open('input.txt')
   input = sys.stdin.readline
   
   for _ in range(int(input())):
       # 명령어 입력
       cmd = input().rstrip()
       # 배열(리스트)의 길이
       length = int(input())
       # 길이가 양수라면, 숫자만 뽑아서 li에 저장
       if length:
           li = list(input()[1:-2].split(','))
       # 길이가 0이하라면 li를 빈 리스트로 초기화
       else:
           _ = input()
           li = []
   
       # 명령어에서 D가 나오는 횟수 계산
       Dcount = cmd.count('D')
       # 배열의 총 길이보다 크다면 error 출력
       if Dcount > length:
           print('error')
       # 배열길이와 같다면 [] 출력
       elif Dcount == length:
           print('[]')
       else:
           # R을 기준으로 명령어 잘라서 Dlist에 연결된 D들의 길이를 저장
           Dlist = list(map(len, cmd.split('R')))
           # 왼쪽에서 잘라낼 개수
           popLeft = sum(Dlist[0::2])
           # 오른쪽에서 잘라낼 개수
           popRight = sum(Dlist[1::2])
   
           if popRight:
               li = li[popLeft:-popRight]
           # 오른쪽에서 하나도 뽑지 않아서 popRight가 0일 경우
           else:
               li = li[popLeft:]
   
           # R이 홀수개 였을 경우 마지막에 한번 리스트 뒤집음
           if len(Dlist) % 2 == 0:
               li.reverse()
   
           # 출력
           print('[' + ','.join(li) + ']')
   ```
   
3. 해설

   - 명령어를 R기준으로 잘라서 삭제되는 요소들이 어디서 사라지는지, 그리고 최종 결과물을 뒤집어야되는지 아닌지를 판별한 아이디어
   - 이외에도 위쪽에서 바로바로 분기처리 or 리턴을 해서 실행시간이 좀 더 빠른것 같다.

