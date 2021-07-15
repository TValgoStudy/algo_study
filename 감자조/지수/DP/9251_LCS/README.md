### 내 풀이

1. 이렇게 푼 이유?

   - DP의 대표적인 유형(난 몰랐음)
   - 2차원 배열로 두 단어 놓고 비교
   - 일치하는 경우 좌상단 대각선 + 1
   - 불일치 하는 경우 좌, 상 중 최대값

   |      |      | A    | C    | A    | Y    | K    | P    |
   | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
   |      | 0    | 0    | 0    | 0    | 0    | 0    | 0    |
   | C    | 0    | 0    | 1    | 1    | 1    | 1    | 1    |
   | A    | 0    | 1    | 1    | 2    | 2    | 2    | 2    |
   | P    | 0    | 1    | 1    | 2    | 2    | 2    | 3    |
   | C    | 0    | 1    | 2    | 2    | 2    | 2    | 3    |
   | A    | 0    | 1    | 2    | 3    | 3    | 3    | 3    |
   | K    | 0    | 1    | 2    | 3    | 3    | 4    | 4    |

   

2. 실행시간

   - 676ms

3. 코드

   ```python
    import sys
    sys.stdin = open('input.txt')
    
    A = input()
    B = input()
    
    N = len(A)
    M = len(B)
    
    DP = [[0] * (M+1) for _ in range(N+1)] # 2차원배열
    
    for a in range(1, N+1):
        for b in range(1, M+1):
            if A[a-1] == B[b-1]: # 두개가 같으면 좌상단 + 1
                DP[a][b] = DP[a-1][b-1] + 1
            else: # 다르면 좌, 상 중에 큰것
                DP[a][b] = max(DP[a][b - 1], DP[a-1][b])
    
    print(DP[-1][-1])
   ```



### 다른 사람의 풀이

1. 실행시간

   - 188ms

2. 코드

   ```python
   def s():
       s1, s2 = input(), input()
       dp = [0] * 1000
       for i in range(len(s1)):
           max_dp = 0
           for j in range(len(s2)):
               if max_dp < dp[j]:
                   max_dp = dp[j]
               elif s1[i] == s2[j]:
                   dp[j] = max_dp + 1
       print(max(dp))
   s()
   
3. 해설

   - 위 표에서도 볼 수 있듯이 아래로 내려가면서 일치할 경우에만 지금까지 나온 값중에 최대값 + 1 하고 있음
   - 일차원 배열로 한줄만 가지고 갱신한다고 보면 됨

