# 1759 암호 만들기

문제를 읽어보다 암호가 3 <= L <= 15인 L개의 알파벳 소문자로 구성되며, 암호로 사용했을 법한 C개의 문자가 주어지고 이 역시 그 크기가 크지 않다는 점에 주목했다.

예를 들어 입력이 다음과 같으면,

```
4 6 
a t c i s w
```

알파벳 네 개로 이루어진 암호가 6개의 알파벳 소문자(a, t, c, i, s, w) 중에서 네 개를 뽑아서 만들어진다는 뜻이다.



그냥 냅다 combinations를 itertools에서 import 해서 써야겠다고 생각하고 시키는 그대로 풀어보았더니 맞긴 맞았다.

## 내 풀이

```python
# 암호는 L개의 알파벳 소문자들로 구성
# 최소 한 개의 모음(a, e, i, o u)과 최소 두 개의 자음으로 구성
# 암호는 알파벳 순서대로 구성됨
# C개의 문자들이 주어졌을 때, 가능성 있는 암호들을 모두 구하는 프로그램
import sys
from itertools import combinations
sys.stdin = open('input.txt')

L, C = map(int, input().split())
chars = list(input().split())
consonants = []
vowels = []
for i in range(C):
    if chars[i] in 'aeiou':
        vowels.append(chars[i])
    else:
        consonants.append(chars[i])
total_vowels = len(vowels)
total_consonants = len(consonants)
# 이제 모음에서 하나를, 자음에서 두 개를 뽑는다.
vs = list(combinations(vowels, 1))
cs = list(combinations(consonants, 2))
remains_cnt = L-3 # 남은 뽑을 개수
answer = []
# 삼중 for문..
for v in vs:
    for c in cs:
        remains = []
        for k in range(C):
            if chars[k] not in v+c: # 이미 뽑은 문자가 아니라면
                remains.append(chars[k]) # 골라줄 문자를 따로 모아줌
        rs = list(combinations(remains, remains_cnt))
        for r in rs:
            result = v+c+r # 가능한 조합 만들기
            result = sorted(list(result)) # 정렬
            result = ''.join(result)
            answer.append(result)
answer = sorted(list(set(answer)))
for ans in answer:
    print(ans)
```

152ms



이렇게 풀면서 이게 최선은 아닌 것 같다는 생각이 들었고, 다른 사람 풀이를 찾아보니 다음과 같이 풀었다.

```python
from itertools import combinations
L,C = map(int, input().split())
targets=sorted(input().split())
v = set(['a','e','i','o','u'])
for comb in combinations(targets,L): # L개를 중복 없이, 순서 상관 없이 뽑는 모든 경우
    cnt= len(set(comb)&v) # comb와 v의 교집합
    if cnt ==0 or len(comb)-cnt<2: # 모음이 뽑히지 않았거나, L에서 모음 수를 뺀 값(자음 수)이 2개 이하로 뽑혔다면
        continue # 아무것도 하지 않고 넘어감
    print(''.join(comb)) # 제대로 뽑혔으면 출력!
```

100ms

교집합을 이용한 풀이였다. 집합을 이용한다는 생각은 평소에 한 적이 없어서 새로웠다.



