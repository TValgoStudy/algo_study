# 1766 문제집



## 1. 위상 정렬?

https://m.blog.naver.com/ndb796/221236874984

- 순서가 정해져있을 때 작업을 정확하게 정렬해주는 알고리즘

- 위상 정렬 자체의 답은 여러 개일 수 있다.

- 명백한 시작점이 존재해야 위상정렬 할 수 있다.



##### 큐를 이용한 위상정렬

1.  진입차수가 0인 정점을 큐에 삽입
2. 큐에서 원소를 꺼내 연결된 모든 간선 제거
3. 간선 제거 이후에 진입차수가 0이 된 정점을 큐에 삽입
4. 큐가 빌 때까지 2~3 과정을 반복, 모든 원소를 방문하기 전에 큐가 빈다면 사이클이 존재 (위상 정렬 불가능), 모든 원소를 방문했다면 큐에서 꺼낸 순서가 위상 정렬의 결과!



여기서 진입차수란 그래프를 그렸을 때 노드를 가리키는 간선의 개수라고 할 수 있다.

특정 노드로 이동하는 경로가 몇 개인지?



이 문제는 이런 위상 정렬에 정해진 하나의 답을 만들어주기 위해 가능한 한 번호 순으로 문제를 풀어준다는 단서를 달아놓았다. 따라서 큐가 아니라 heap에 문제 번호를 넣어 풀어주어야 한다.

## 2. 내 풀이(시간 초과)

아래와 같이 풀면 풀리긴 하지만 코드를 쓰면서도 안 될 것은 알았다. 100,000개나 되는 케이스에 이 정도 연산을 하면 당연히 안될 것 같았음. 하지만 아마도 답은 나올 것이다.

```python
import sys
import heapq
sys.stdin = open('input.txt')

# 위상정렬 + heap 이용하는 문제라고 함
N, M = map(int, input().split()) # N은 32000 이하, M은 100,000 이하
result = [] # 답이 들어갈 배열
heap = []
numbers = {}
linked = [[] for _ in range(N+1)]
for i in range(1, N+1):
    numbers[i] = []

for _ in range(M):
    a, b = map(int, input().split()) # a가 b를 가리킴(a를 먼저 푸는 것이 좋음)
    numbers[b].append(a) # key b에는 a가 추가됨(b 숫자의 진입 차수를 알기 위해 만듦)
    linked[a].append(b) # a번 배열에는 b가 추가됨(a가 큐에서 꺼내지면 어떤 노드와의 연결을 끊을지 알기 위해 만듦)
# 1. 진입차수가 0인 수 먼저 heap에 넣어주기
for i in range(1, N+1):
    if not numbers[i]:
        heapq.heappush(heap, i)
        del numbers[i]

while heap:
    # heap에서 숫자 하나를 꺼내고 해당 문제를 선행 문제로 하는 경우의 간선을 끊어준다.
    a = heapq.heappop(heap)
    bs = linked[a] # a가 가리키는 수들
    result.append(a)
    for b in bs:
        numbers[b].remove(a)
    # 어떤 간선을 끊었는지 저장하기 위한 배열
    delete_nums = []
    for key in numbers.keys():
        # 만약 더 이상 선행문제가 없으면(진입차수가 0이면) heap에 넣어주기
        if not numbers[key]:
            heapq.heappush(heap, key)
            delete_nums.append(key)
    # heap에 넣어준 문제는 남은 문제에서 삭제 
    for num in delete_nums:
        del numbers[num]

for i in range(len(result)):
    print(result[i], end=' ')
```



그렇다면 진입차수를 보다 간단히 표현하는 방법이 있을까?

나는 key (a값)에 해당하는 value가 [] 배열이면 진입차수를 0으로 보았지만,

그냥 진입차수를 숫자로 만들어주고, pop을 할 때 해당 문제에 연결된 문제의 진입차수를 1씩 빼주면 **배열의 연산이 필요 없어진다.**



## 다른 사람의 풀이

https://alpyrithm.tistory.com/113 참고

```python
import sys
import heapq
sys.stdin = open('input.txt')

# 위상정렬 + heap 이용하는 문제라고 함
N, M = map(int, input().split())
heap = []
result = [] # 결과를 담을 배열
problems = [0 for _ in range(N+1)] # N개 문제의 진입차수 (0번째는 무시할 것)
a_to_b = {}
for _ in range(M):
    a, b = map(int, input().split()) # a를 풀고 b를 풀어야 함
    # 필요한 것: a와 연결된 문제들의 정보, b의 진입차수
    # a를 선행 문제로 가지는 b는 진입 차수가 하나 늘어난다.
    # a를 키로, [b1, b2, b3, ...]를 value로 하는 dictionary를 만든다.
    problems[b] += 1
    if a_to_b.get(a):
        a_to_b[a].append(b)
    else:
        a_to_b[a] = [b]

# 풀이법
# 진입 차수가 0인 problem을 heap에 넣는다.
# 하나 꺼낸 후 해당 문제 key와 연결된 b1, b2, b3, ...의 진입 차수를 줄여준다.
# 다시 진입 차수가 0인 문제를 넣어준다.
# heap이 빌 때까지 반복

# 초기 설정: 진입 차수가 0인 problem을 heap에 넣음
for i in range(1, N+1):
    if problems[i] == 0:
        heapq.heappush(heap, i)
# heap이 빌 때까지 반복
while heap:
    # 문제 하나 꺼내고
    a_pop = heapq.heappop(heap)
    # 그 문제가 다른 문제의 선행 문제라면
    if a_to_b.get(a_pop):
        # 다른 문제들의 진입 차수를 하나 줄이고 0인지 확인, 0이면 heap에 넣기
        for b in a_to_b[a_pop]:
            problems[b] -= 1
            if problems[b] == 0:
                heapq.heappush(heap, b)

    result.append(a_pop)
print(*result)
```

pypy 400ms 풀이



속도의 차이는 readline을 사용한 것의 차이인듯, 가장 빠른 풀이는 240ms 였다.

