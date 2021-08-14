### 내 풀이

1. 이렇게 푼 이유?

   - 프로그래머스에 비슷한 문제가 있음 [큰 수 만들기](https://programmers.co.kr/learn/courses/30/lessons/42883) 아니 지금보니까 인풋도 똑같네
   - 근데 프로그래머스 풀이는 문제 카테고리가 그리디여서 요상하게 풀어서 그런지 백준 돌려보니까 시간초과남

2. 실행시간

   - 248ms (python)

3. 코드

   ```python
    import sys
    sys.stdin = open('input.txt')
    input = sys.stdin.readline
    
    
    def solution():
        n, k = map(int, input().split())
        arr = input()
        stack = []
        rmv = k
        l = 0
    
        for a in arr:
            while stack and stack[-1] < a and rmv > 0:
                stack.pop()
                rmv -= 1
                l -= 1
            stack.append(a)
            l += 1
    
            if l > n - k:
                break
    
        return ''.join(stack[:n-k])
    
    print(solution())
   ```



### 다른 사람의 풀이

1. 실행시간

   - 172ms / [dau47](https://www.acmicpc.net/source/30033658) 

2. 코드

   ```python
    from sys import stdin
    readline = stdin.readline
    
    N, K = map(int, readline().split())
    numbers = readline().rstrip()
    
    def solve():
        global K
        stack = []
        for number in numbers:
            while stack and K and stack[-1] < number:
                stack.pop()
                K -= 1
            stack.append(number)
        
        while K:
            stack.pop()
            K -= 1
    
        print(''.join(stack))
    solve()
   ```

3. 해설

   - 슬라이싱으로 한거보다 while pop이 더 빠르다