# 1744 수 묶기

## 내 풀이

```python
# 최대..
N = int(input())
plus_numbers = []
minus_numbers = []
zeros = []
for _ in range(N):
    num = int(input())
    if num > 0:
        plus_numbers.append(num)
    elif num == 0:
        zeros.append(0)
    else:
        minus_numbers.append(num)
# 1은 그냥 더해주는게 나음
# -값은 두 개 이상이면 서로 묶어주고, 하나면 그냥 더하는게 나음
plus_numbers.sort()
minus_numbers.sort(reverse=True)

result = []
if len(zeros) > 0: # 0이 있을 때
    if len(minus_numbers) % 2: # -값의 개수가 홀수면
        minus_numbers.pop(0) # 0을 곱해주는 것과 같은 효과
        zeros.pop()
while plus_numbers:
    num1 = plus_numbers.pop()
    if plus_numbers:
        num2 = plus_numbers.pop()
        if num1 * num2 > num1 + num2:
            result.append(num1 * num2)
        else:
            result.append(num1+num2)
    else:
        result.append(num1)

while minus_numbers:
    num1 = minus_numbers.pop()
    if minus_numbers:
        num2 = minus_numbers.pop()
        result.append(num1 * num2)
    else:
        result.append(num1)
print(sum(result))
```

