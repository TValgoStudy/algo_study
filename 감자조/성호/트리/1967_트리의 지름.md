# 1967_트리의 지름



## 나의 풀이

```python
# 메모리 초과 adj graph 풀이

import sys
sys.stdin = open('input.txt')


import heapq

def dijkstra(i):
    dist[i] = 0
    heap = []
    heapq.heappush(heap, (dist[i], i))

    while heap:
        w, s = heapq.heappop(heap)
        for e in range(n+1):
            if graph[s][e]:
                if dist[e] > dist[s] + graph[s][e]:
                    dist[e] = dist[s] + graph[s][e]
                    heapq.heappush(heap, (dist[e], e))


n = int(input())
edges = []
graph = [[0]*(n+1) for _ in range(n+1)]
for _ in range(n-1):
    s, e, w = map(int, input().split())
    graph[s][e] = w
    graph[e][s] = w

result = []
# 어떤 두 노드 사이의 거리 구하기(다익스트라)
dist = [987654]*(n+1)
dijkstra(1)
# dist에는 1번에서 가장 먼 노드가 주어짐
max_val = 0
max_idx = 1
for idx, val in enumerate(dist[1:]):
    if val > max_val:
        max_idx = idx
        max_val = val

# 두 번째 다익스트라
dist = [987654]*(n+1)
dijkstra(max_idx+1) # dist에서 0번을 빼고 찾은 max_idx 이므로 1 더하기
print(max(dist[1:]))
```

다익스트라로 풀면 될 것 같아서 처음에는 노드 개수만큼 다익스트라를 돌았는데, 당연히 메모리 초과가 뜨길래 검색을 해봤다. 그런데 두 번의 다익스트라로 지름을 구할 수 있다고 하여 잘 이해는 안가지만 한번 해봤는데, 마찬가지로 메모리 초과가 떴다. 

이유: 그래프로 했더니 불필요한 순회가 너무 많음!



노드의 개수가 많아지면 인접 리스트를 만들어서 풀어야 함

```python
# 324ms adj list 풀이
import heapq

def dijkstra(i):
    dist[i] = 0 # 자기 자신으로 향하는 거리
    heap = []
    heapq.heappush(heap, (dist[i], i)) # 초기화

    while heap:
        w, j = heapq.heappop(heap)
        for k in range(len(adj_list[j])): # 인접 리스트의 배열 길이만큼 순회
            w_new, j_new = adj_list[j][k]
            if dist[j_new] > dist[j] + w_new:
                dist[j_new] = dist[j] + w_new
                heapq.heappush(heap, (dist[j_new], j_new))


n = int(input()) # 노드의 개수

# 딕셔너리로 인접리스트 만들기
adj_list = [[] for _ in range(10001)]
# 주어지는 정보: (부모 노드, 자식 노드, 가중치)
for _ in range(n-1):
    p, c, w = map(int, input().split())
    adj_list[p].append((w, c))
    adj_list[c].append((w, p)) # 반대 방향

# print(adj_list)
# adj_list = [[], [(3, 2), (2, 3)], [(3, 1), (5, 4), ...]
dist = [987654321]*(n+1)
dijkstra(1) # 첫 번째 다익스트라

max_val = 0
max_idx = 0
dist[0] = 987654321 # 987654321을 배제
for idx, val in enumerate(dist[1:]):
    if val > max_val:
        max_idx = idx
        max_val = val
dist = [987654321]*(n+1) # 배열 다시 만들기
dijkstra(max_idx+1)
print(max(dist[1:]))
```



딕셔너리로도 만들어서 풀어봤는데 100%에 다 와서 keyError가 뜬다.

```python
# adj_dict 풀이, keyError
import heapq

def dijkstra(i):
    dist[i] = 0 # 자기 자신으로 향하는 거리
    heap = []
    heapq.heappush(heap, (dist[i], i)) # 초기화

    while heap:
        w, j = heapq.heappop(heap)
        for k in range(len(adj_list[j])): # 인접 리스트의 배열 길이만큼 순회
            w_new, j_new = adj_list[j][k]
            if dist[j_new] > dist[j] + w_new:
                dist[j_new] = dist[j] + w_new
                heapq.heappush(heap, (dist[j_new], j_new))


n = int(input()) # 노드의 개수

# 딕셔너리로 인접리스트 만들기
adj_list = {}
# 주어지는 정보: (부모 노드, 자식 노드, 가중치)
for _ in range(n-1):
    p, c, w = map(int, input().split())
    if adj_list.get(p):
        adj_list[p].append((w, c))
        if adj_list.get(c):
            adj_list[c].append((w, p)) # 반대 방향
        else:
            adj_list[c] = [(w, p)]
    else:
        adj_list[p] = [(w, c)]
        if adj_list.get(c):
            adj_list[c].append((w, p)) # 반대 방향
        else:
            adj_list[c] = [(w, p)]
# adj_list = {1: [(3, 2), (2, 3)], 2: [(3, 1), (5, 4)], ...}
dist = [987654321]*(n+1)
dijkstra(1) # 첫 번째 다익스트라

max_val = 0
max_idx = 1
for idx, val in enumerate(dist[1:]):
    if val > max_val:
        max_idx = idx
        max_val = val
dist = [987654321]*(n+1) # 배열 다시 만들기
dijkstra(max_idx+1)
print(max(dist[1:]))
```





## 다른 사람 풀이

```python
def main():
    n = int(input())
    adj = [[] for _ in range(n+1)]
    ans = [(0,0)] * (n+1)
    for _ in range(n-1):
        p,c,w = map(int,input().rstrip().split())
        adj[p].append((c,w))
    for i in range(n,0,-1):
        mx,mx2 = 0,0
        for v,w in adj[i]:
            t = w + ans[v][0]
            if t > mx:
                mx2 = mx
                mx = t
            elif t > mx2:
                mx2 = t
        ans[i] = (mx,mx2)
    ans.sort(reverse=True, key = lambda x: sum(x))
    print(sum(ans[0]))
if __name__ == '__main__':
    main()
```

?? 뭔지 잘 모르겠다.

