### 내 풀이

1. 해설, 포인트

   - 부모 정보로 들어오는 인풋으로 자식리스트를 구함
   - DFS로 모든 노드를 순회하면서, 자식이 없는 노드의 수를 더함
   - 만약 해당 노드가 삭제할 노드라면, 삭제 노드의 부모의 자식수가 1개면 리프노드가 된 것이므로 +1

2. 실행시간

   - python : 76ms

3. 코드

   ```python
    def findChild():
        temp = [[] for _ in range(N)]
        root = 0
    
        for n in range(N):
            if P[n] != -1:
                temp[P[n]].append(n)
            else:
                root = n # root가 0인줄 알았으나 문제에선 그런말 한적 없음
    
        return temp, root
    
    
    def DFS(n):
        global answer
    
        if n == removeNode: # 제거할 노드일 때
            if len(child[P[n]]) == 1: # 형제노드가 없으면 부모가 리프 노드가 되므로
                answer += 1
            return
    
        if not child[n]:
            answer += 1
            return
    
        for m in child[n]:
            DFS(m)
    
    
    N = int(input())
    P = list(map(int, input().split()))
    removeNode = int(input())
    child, root = findChild()
    answer = 0
    
    DFS(root)
    print(answer)
   ```

<br/>




### 다른 사람의 풀이

1. 실행시간

   - 56ms

2. 코드

   ```python
    import sys
    input=sys.stdin.readline
    
    
    N=int(input())
    nodes=[[] for  i in range(N)]
    for idx,p in enumerate(map(int,input().split())):
        if p==-1: continue
        nodes[p].append(idx)
    
    rem=int(input())
    
    def remove(rem):
        for i in nodes[rem]:
            remove(i)
        nodes[rem]=None
    
    
    remove(rem)
    
    print(sum([1 if i in([],[rem]) else 0 for i in nodes]))

   ```

3. 해설

   - 첫번째 반복문으로 해당 노드의 자식 노드 구하기
   - remove 함수로 삭제할 노드와, 삭제할 노드의 서브트리를 모두 제거
   - 자식 노드가 [] : 없거나, [rem] : rem만 남았으면 1 / 아니면 0