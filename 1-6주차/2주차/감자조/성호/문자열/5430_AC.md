# 5430_AC



## 내 풀이

```python
import sys
sys.stdin = open('input.txt')

from collections import deque
T = int(input())

for tc in range(1, T+1):
    p = input()
    n = int(input())
    data = input()
    data = data[1:-1] # 앞뒤 괄호 제거
    data = data.split(',')

    if data[0] != '':
        data = list(map(int, data))
    elif data[0] == '': # 맨 처음 비어있으면
        data.pop() # 문제1. 여기서 error를 프린트하고 다음 경우로  넘어가도록 했었음

    data = deque(data)
    reverse = False
    error = False
    for i in range(len(p)):
        if p[i] == 'R': # 여기서 data가 비어있지 않다는 조건도 넣었었음
            # 진짜 뒤집는거보단 인덱스 바꾸기
            if reverse == False:
                reverse = True
            else:
                reverse = False
        elif p[i] == 'D' and data:
            if reverse: # 거꾸로 된 상태라면
                data.pop()
            else: # 원래대로면
                data.popleft()
        else: # 데이터가 비어 있고 D면
            error = True
            break

    if error:
        print('error')
    else:
        data = list(data)
        if reverse == True:
            data = data[::-1]
        data = list(map(str, data))
        data = ','.join(data)
        result = '[' + data + ']'
        print(result)

# 원인: 빈 배열에 대해 D가 아니라 R일 때도 error가 발생하도록 만들었음

# 속도: 384ms
```



## 다른 사람 풀이([res1235](https://www.acmicpc.net/user/res1235))

```python
def BOJ_5430():
    for _ in range(int(input())):
        p = input().replace('RR', '') # 찾을 값, 바꿀 값
        # RR은 결국 아무 동작도 안한거나 마찬가지이므로 삭제
        n = int(input()) # 배열에 들어있는 수의 개수 n
        i, j, is_reverse = 0, 0, False
		
        # 수행할 함수를 먼저 전부 확인..
        for f in p:
            if f == "R":
                is_reverse = not is_reverse
            elif f == "D":
                if not is_reverse: # D인데 안 뒤집어져있으면 i += 1
                    i += 1
                else:
                    j += 1 # D인데 뒤집어져 있으면 j += 1
		
        dq = input()[1:-1].split(',')[i:n-j] 
        # [1,2,3,4] => '1,2,3,4' => ['1', '2', '3', '4'][i:n-j]
        
        if i+j <= n: # 삭제한 개수가 n개 이하일 때
            if not is_reverse: # 뒤집어져 있지 않으면
                print('['+','.join(dq)+']') # 그대로 출력
            else:
                print('['+','.join(dq[::-1])+']') # 뒤집어서 출력
        else: # n개를 초과하여 삭제를 시도할 때
            print("error")
BOJ_5430()

# 속도: 124ms
```

나도 나름대로 pop을  쓸데없이 쓰지는 않았다고 생각했는데, 앞부분을 삭제하는 인덱스와 뒷부분을 삭제하는 인덱스를 나눠서 굳이 pop을 하지 않고 해결, 여기에 더해서 i+j로 삭제한 개수를 표현한게 대단하다.

