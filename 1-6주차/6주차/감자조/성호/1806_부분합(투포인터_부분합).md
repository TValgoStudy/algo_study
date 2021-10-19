# 1806_부분합



## 1. 시간 초과 풀이

```python
import sys
sys.stdin = open('input.txt')

N, S = map(int, input().split())
# 비교 대상 하나를 고른 후 다 해보기? => 너무 오래 걸릴듯
# 투 포인터
numbers = list(map(int, input().split()))
start = 0
end = 1
ans = 0 # 만들 수 없으면 ans = 0
min_L = 1000001
while start < N and end <= N:
    if sum(numbers[start:end]) >= S:
        L = end - start # 길이
        if L < min_L:
            min_L = L
        start += 1
    else:
        end += 1

if min_L == 1000001:
    print(ans)
else:
    print(min_L)
```

sum을 남발



## 2. 현재 위치까지의 합 구하고 풀기

```python
import sys
sys.stdin = open('input.txt')

N, S = map(int, input().split())
numbers = [0] + list(map(int, input().split())) # 합은 0부터 시작
num_sum = [0] * (N+1)
for i in range(1, N+1):
    num_sum[i] = num_sum[i-1] + numbers[i]
# print(num_sum) => [0, 5, 6, 9, 14, 24, 31, 35, 44, 46, 54]

start = 0
end = 1
ans = 0
min_L = 1000001
while end < N+1 and start < N:
    if num_sum[end] - num_sum[start] >= S:
        L = end - start
        start += 1
        if L < min_L:
            min_L = L
    else:
        end += 1
if min_L == 1000001:
    print(ans)
else:
    print(min_L)
```

172ms

1. 리스트의 맨 앞에 [0]을 추가해준다.
2. 리스트의 i번째 값이 i번째 값 까지의 합인 num_sum을 만든다.
3. 투 포인트 알고리즘 적용!
   1. start = 0, end = 1로 초기 설정
   2. end - start가 S보다 크거나 같으면 조건을 만족하므로 start를 1 늘리고 해당하는 부분합의 길이 L을 min_L과 비교
   3. end - start가 S보다 작으면 end를 1 늘림



투포인트 알고리즘이 뭔가 했는데, 직접 손으로 써보니까 확실히 알겠다.



5 1 3 5 10 7 4 9 2 8



=> 0 5 6 9 14 24 31 35 44 46 54



=> 5 - 0 = 5 < S 이므로 end += 1

=> 6 - 0 = 6 < S 이므로 end += 1

=> 9 - 0 = 9 < S 이므로 end += 1

=> 14 - 0 = 14 < S 이므로 end += 1

=> 24 - 0 = 24 > S 이므로 start += 1, len = 5 갱신

=> 24 - 5 = 19 > S 이므로 start += 1, len = 4 갱신

=> 24 - 6 = 18 > S 이므로 start += 1, len = 3 갱신

=> 24 - 9 = 15 = S 이므로 end += 1, len = 2 갱신

=> 31 - 9 = 22 > S 이므로 start += 1, len = 3

=> 31 - 14 = 17 > S 이므로 start += 1, len = 2

...