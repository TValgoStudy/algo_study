# 2887 행성 터널



처음 생각: combination을 이용해서 모든 경우의 min 값을 구해야 하나?

=> 최대 100,000개의 행성

[combination의 시간복잡도 = O(nCr)](https://stackoverflow.com/questions/53419536/what-is-the-computational-complexity-of-itertools-combinations-in-python)

우리 경우에는 nC2 = O(n(n-1)/2) = O(n^2) 이므로 사용해선 안된다.

컴퓨터의 평균 연산 능력이  1초에  8.5×10^7 회라고 하니, 이에 따르면 약 59초의 시간이 필요하다.



못 풀고 그냥 찾아본 결과, x, y, z 각각에 대해 오름차순 정렬한 후 |x_a - x_b|, |y_a - y_b|, |z_a - z_b|를 계산하여 새로운 list에 추가해 준 후, 다시 min값이 작은 순으로 정렬한 후 kruskal을 적용하였다.

[sort의 시간 복잡도는 O(nlogn)](https://wayhome25.github.io/python/2017/06/14/time-complexity/) 으로, 10만개의 데이터가 있다고 하면 

예를 들어, 아래와 같은 데이터가 있다고 하면 약 1,151,292로, 실제로는 0.0135초면 된다.

```
11 -15 -15
14 -5 -15
-1 -1 -5
10 -4 -1
19 -4 19
```



1) x가 작은 순으로 정렬

```
-1 -1 -5
10 -4 -1
11 -15 -15
14 -5 -15
19 -4 19
```



2) 순서대로 x 좌표의 차(abs(x1-x2))를 구하여 tunnel에 추가

```
tunnel = [11, 1, 3, 5]
```



3) y가 작은 순으로 정렬

```
11 -15 -15
14 -5 -15
10 -4 -1
19 -4 19
-1 -1 -5
```



4) 순서대로 y 좌표의 차를 구하여 tunnel에 추가

```
tunnel = [11, 1, 3, 5, 10, 1, 0, 3]
```



5) z가 작은 순으로 정렬

```
11 -15 -15
14 -5 -15
10 -4 -1
-1 -1 -5
19 -4 19
```



6) 순서대로 z 좌표의 차를 구하여 tunnel에 추가

```
tunnel = [11, 1, 3, 5, 10, 1, 0, 3, 0, 14, 4, 24]
```



7) tunnel을 오름차순 sort 하고 kruskal 적용

이 때 물론 tunnel의 데이터에는 해당 비용이 어떤 좌표 둘을 연결한 비용인지에 대한 정보도 함께 들어있어야 한다. (위에서는 표시하지 않았음)

```
tunnel = [0, 0, 1, 1, 3, 3, 4, 5, 10, 11, 14, 24] (좌표도 함께 묶여있을 것)
=> kruskal
```



# 풀이(1952ms)

```python
import sys

sys.stdin = open('input.txt')

def find_set(x):
    if p[x] != x:
         p[x] = find_set(p[x])
    return p[x]

def union(x, y):
    p[find_set(y)] = find_set(x)

N = int(input())

locations = []
for i in range(N):
    x, y, z = map(int, input().split())
    locations.append((x, y, z, i)) # 순서까지 매겨서 위치 추가

# x의 최소 비용
locations.sort()
tunnel = [] # 통로
for i in range(N-1):
    tunnel.append((abs(locations[i][0] - locations[i+1][0]), locations[i][3], locations[i+1][3]))
# y의 최소 비용
locations.sort(key=lambda x: x[1])
for i in range(N-1):
    tunnel.append((abs(locations[i][1] - locations[i+1][1]), locations[i][3], locations[i+1][3]))
# z의 최소 비용
locations.sort(key=lambda x: x[2])
for i in range(N-1):
    tunnel.append((abs(locations[i][2] - locations[i+1][2]), locations[i][3], locations[i+1][3]))

p = [i for i in range(N)]

tunnel.sort()
# print(tunnel)
cnt = 0
i = 0
ans = 0
while cnt < N-1:
    if find_set(tunnel[i][1]) != find_set(tunnel[i][2]): # 부모가 같지 않으면
        union(tunnel[i][1], tunnel[i][2])
        ans += tunnel[i][0]
        cnt += 1
        i += 1
    else:
        i += 1
print(ans)
```



#### 주의

find_set을 while문으로 작성하면 시간초과가 난다. 이미 부모를 찾아 본 경우에도 계속 찾아봐야 해서 그런 것 같고, 위처럼 find_set을 할 때 부모 노드를 바꿔주면 여러 번 계산하지 않게 되어 통과된다.

```python
def find_set(x):
    while p[x] != x:
        x = p[x]
    return x
p를 건드리지 않고 부모만 반환해 줌


def find_set(x):
    if p[x] != x:
         p[x] = find_set(p[x])
    return p[x]
p[x]를 계속 갱신하면서 부모를 찾아감
```

