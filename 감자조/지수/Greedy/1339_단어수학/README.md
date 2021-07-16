### 내 풀이

2. 실행시간
   - 76ms

3. 코드

   ```python
   import sys
   sys.stdin = open('input.txt')
   
   # 자릿수가 다른 경우
   # ACDEB
   # 00GCF
   # 자릿수가 큰걸 무조건 큰 숫자로?
   # 10000*A + (1000+10)*C + 100*G + 100*D + 10*E + 1*B + 1*F
   
   # 76ms
   
   N = int(input())
   
   alphaList = {}
   numList = []
   result = 0
   n = 9
   
   for _ in range(N):
       s = input()
       SL = len(s)
       for i in range(SL):
           alphaList[s[i]] = alphaList.get(s[i], 0) + 10**(SL-i-1)
   
   
   for key, val in alphaList.items():
       numList.append((val, key))
   numList.sort(reverse=True)
   
   
   for chasu, gyesu in numList:
       result += chasu * n
       n -= 1
   
   print(result)
   ```
   

3. 해석
   - 처음엔 식을 `10000*A + 1000*C + 100*(G+D) + 10*(E+C) + 1*(B+F) `이런식(알파벳 기준)으로 풀어내려다 틀림
   - 나중에는 `10000*A + (1000+10)*C + 100*G + 100*D + 10*E + 1*B + 1*F ` 이렇게 자릿수 기준으로 접근



### 다른 사람의 풀이

1. 실행시간

   - 56ms

2. 코드

   ```python
   n=int(input())
   w,r,s=[0]*26,0,9
   for i in range(n):
   	ii=input()
   	for i in range(len(ii)):
   		w[ord(ii[i])-ord('A')]+=10**(len(ii)-i-1)
   w.sort(reverse=True)
   for i in w:
   	r,s=r+i*s,s-1
   print(r)
   ```
   
3. 해설

   - 로직은 동일한데 알파벳 크기만큼 고정 리스트를 만들어서 알파벳 필요 없이 값 하나만 가지고 정렬해서 빠른듯. (내꺼는 기준 2개)

