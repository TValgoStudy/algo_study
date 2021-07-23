### 내 풀이

1. 해설, 포인트

   - 양수의 경우 큰것 두개씩 묶는게 최대값을 만듬
   - 음수의 경우 가장 작은(절대값이 큰)것 두개를 곱하면 절대값이 최대가 되고 양수가 됨
   - 음수가 홀수개로 남을 경우 0이 있다면 곱해서 0을 만들수 있고, 없다면 묶지 않고 더해야함
   - 헷갈렸던 조건 `1`!
   - 양수의 경우 1은 다른 수와 곱하는 것보다 더하는게 최대임! 

2. 실행시간

   - python : 72ms

3. 코드

   ```python
    N = int(input())
        
    plus = []
    minus = []
    one = 0 # 처음에 생각하지 못한 조건
    zero = 0
    result = 0
    
    for _ in range(N):
        num = int(input())
        if num > 1:
            plus.append(num)
        elif num == 1:
            one += 1
        elif num == 0:
            zero += 1
        else:
            minus.append(num)
    
    # 절대값이 큰순 ~ 작은순으로 정렬
    plus.sort(reverse=True)
    minus.sort()
    
    P = len(plus)
    M = len(minus)
    
    # 큰수 두개씩 곱
    for i in range(0, P//2):
        result += plus[2*i] * plus[2*i+1]
    
    # 홀수개면 마지막것도 더하기
    if P % 2:
        result += plus[-1]
    
    # 음수도 두개 짝지어서 곱
    for j in range(0, M//2):
        result += minus[2*j] * minus[2*j+1]
    
    # 홀수개고, 0도 없으면 더해져야 함
    if M % 2 and zero == 0:
        result += minus[-1]
    
    result += one # 1은 곱한 것보다 더한게 큼 : 3*1 < 3+1
    
    print(result)

   ```

<br/>




### 다른 사람의 풀이

1. 실행시간

   - 56ms

2. 코드

   ```python
    import sys
    n = int(input())
    arr1 = []
    arr2 = []
    arr3 = []
    ret =0 
    for _ in range(n):
        x = int(sys.stdin.readline())
        if x<1: arr1.append(x)        
        elif x>1:arr2.append(x)
        else: arr3.append(x)
    arr1.sort()
    arr2.sort()
    for i in range(0,len(arr1)-1,2):
        ret+=arr1[i]*arr1[i+1]
    if len(arr1)%2 == 1: ret+=arr1[-1]
    for i in range(len(arr2)-1,0,-2):
        ret+=arr2[i]*arr2[i-1]
    if len(arr2)%2 == 1: ret+=arr2[0]
    ret+=sum(arr3)
    print(ret)

   ```

3. 해설

   - 1보다 작은것, 큰것, 1인것으로 나누어서 곱곱합합
   - 음수안에 0도 포함하게 해서 그냥 바로 짝지어서 곱해지게 하니 0을 따로 구할 필요 없음