# 2839_설탕배달



## 1. 나의 풀이

```python
import sys
sys.stdin = open('input.txt')

N = int(input())

# N = 5x + 3y
# N//5 <= x + y <= N//3
# x + y = k 라고 할 때, 
# x = (N-3k) / 2
# y = 5k/2 - N/2

# k값을 바꿔가며 답을 찾는다.
result = -1
flag = False
for k in range(N//5, (N//3)+1):
    x = (N-3*k)//2
    y = 5*k//2 - N//2
    while 0 <= x and 0<= y:
        # 만약 답이라면 5x+3y = N이 나옴
        if 5*x + 3*y == N:
            result = x+y
            flag = True
            break
        else:
            break
    if flag:
        break
print(result)

# 68ms
```

3kg 봉지와 5kg 봉지의 개수에 대한 식을 세워서 풀었다.

- 전체 무게 N= 3kg봉지개수 * 3 + 5kg봉지개수*5

- 5kg봉지에 나눠 담은 개수 <= 봉지 개수(x+y) <= 3kg봉지에 나눠 담은 개수

- x+y = k 라고 하고, x와 y를 N과 k에 대한 식으로 정리한 뒤 k를 범위 내에서 하나씩 확인하여 답을 찾는다.



## 2. 가장 속도가 빠른 답

```python
N = int(input())
cnt = 0
while True:
    if (N % 5) == 0:
        cnt = cnt + (N // 5)
        print(cnt)
        break
    N -= 3
    cnt += 1
    if N < 0:
        print(-1)
        break
# 52ms
```

5의 배수가 될 때까지 3을 뺀다. 설탕 봉지를 5kg으로 나눌 수 있는 최대 수 만큼 나누게 될 것

