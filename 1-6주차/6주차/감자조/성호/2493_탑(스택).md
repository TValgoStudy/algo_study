# 2493_탑



## 시간 초과 풀이

```python
# 500,000개의 이중 루프 => 시간초과

import sys
sys.stdin = open('input.txt')

N = int(input())
towers = list(map(int, input().split()))
answer = [0]*N
for i in range(len(towers)-1, 0, -1):
    for j in range(i-1, 0, -1):
        if towers[i] < towers[j]:
            answer[i] = j+1
            break

print(*answer)
```



## 틀린 풀이

```python
import sys
sys.stdin = open('input.txt')

N = int(input())
towers = list(map(int, input().split()))
answer = [0]*N
L = len(towers)
i = L-1 # 포인터
j = L-2 # 포인터2
tmp = towers[i]
while i >= 0:
    if tmp <= towers[j]:
        for k in range(j+1, i+1):
            answer[k] = j+1
        i -= 1
        j -= 1
        tmp = towers[i]
    elif tmp > towers[j]:
        j -= 1

        if j == -1:
            answer[i] = 0
            i -= 1
            j = i-1
            tmp = towers[i]

print(*answer)
```



## 정답(stack 사용, 오른쪽에서 왼쪽으로)

```python
import sys
sys.stdin = open('input.txt')

N = int(input()) # 탑의 수

towers = list(map(int, input().split()))

# 맨 오른쪽부터 순서대로 스택에 쌓는다.
# 새로운 탑의 높이를 마지막 원소와 비교하여 새로운 탑이 더 크면 꺼낸다.
ans = [0] * N
stack = []
L = len(towers)
stack.append((L-1, towers[-1])) # 초기값(가장 오른쪽 탑의 번호와 높이)
for i in range(L-2, -1, -1): # 역순
    while stack[-1][1] < towers[i]:
        idx, tall = stack.pop()
        ans[idx] = i+1
        if len(stack) == 0:
          break
    stack.append((i, towers[i]))

print(*ans)
```

스택을 사용하면 너무 간단하다.

704ms

## 다른 사람 풀이([axcee](https://www.acmicpc.net/user/axcee), 왼쪽에서 오른쪽으로)

```python
from math import inf
import sys
sys.stdin = open('input.txt')
def sol(ht) :
    ht.insert(0, inf) # 맨 앞에 inf 추가
    st = [0] # 수신탑 역할
    res = []
    for i in range(1, len(ht)) :
        while ht[st[-1]] <= ht[i] :
            st.pop()
        res.append(st[-1]) # 답
        st.append(i)
    ht.pop(0)
    return res

n = int(input())
ht = [int(x) for x in input().split()]
res = sol(ht)
print(' '.join(str(x) for x in res))
```

1. 맨 처음 추가하는 inf가 처음 탑의 수신탑 역할을 한다.
2. res에 답을 하나씩 쌓을 것이다.
3. 가장 가까운 수신탑의 높이보다 현재 탑의 높이가 더 높으면 수신탑은 제 기능을 못하므로 제거(pop)한다.
4. 가장 가까운 수신탑의 높이가 현재 탑 높이보다 더 높으면 그 탑의 위치를 res에 append 해준다.
5. 수신탑 배열(st)에는 현재 탑을 넣어준다.

마지막 ht.pop(0)은 그냥 inf 제거한 것

488ms