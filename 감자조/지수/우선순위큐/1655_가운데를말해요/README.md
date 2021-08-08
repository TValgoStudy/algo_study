### 풀이

1. 이렇게 푼 이유?

   - 그냥 힙쓰면 될거같았는데 뭔가 굉장히 이상했다.
   - 최소힙, 최대힙 두개를 사용
   - 최대힙은 내림차순, 최소힙은 오름차순으로 정렬된다.
   - 최대힙에서 가장 큰 수가, 최소힙의 최소값보다 작으면 ~최~대~힙~,~최~소~힙~ 이런식으로 배치되는것이다.
   - 그러므로 최대힙의 최대값이 중간값이 된다.
   - 1개가 추가 될때마다 `~최~대~힙~,~최~소~힙~` 이대로 배치 되지 않으면 값을 교환하고 있기 때문에 항상 저 순서로 배치된다.

2. 실행시간

   - 304ms (python)

3. 코드

   ```python
    import heapq
    import sys
    sys.stdin = open('input.txt')
    input = sys.stdin.readline
    
    N = int(input())
    
    maxHeap = []
    minHeap = []
    
    for i in range(N):
        val = int(input())
    
        if len(maxHeap) == len(minHeap):
            heapq.heappush(maxHeap, -val)
        else:
            heapq.heappush(minHeap, val)
    
        if minHeap and (-maxHeap[0]) > minHeap[0]:
            MAX = heapq.heappop(maxHeap)
            MIN = heapq.heappop(minHeap)
            heapq.heappush(maxHeap, -MIN)
            heapq.heappush(minHeap, -MAX)
    
        print(-maxHeap[0])
   ```


### 다른 사람의 풀이1

1. 실행시간

   - 188ms

2. 코드

   ```python
    import sys
    import heapq
    
    
    def sol1655():
        maxq, minq = [], []
        n, *nums = map(int, sys.stdin.read().split())
        answer = []
        for num in nums:
            if not maxq or num <= -maxq[0]:
                heapq.heappush(maxq, -num)
            else:
                heapq.heappush(minq, num)
            diff = len(maxq) - len(minq)
            if diff == 2:
                heapq.heappush(minq, -heapq.heappop(maxq))
                diff = 0
            elif diff == -2:
                heapq.heappush(maxq, -heapq.heappop(minq))
                diff = 0
    
            answer.append(str(-maxq[0] if diff >= 0 else minq[0]))
        print('\n'.join(answer))
    
    
    if __name__ == '__main__':
        sol1655()
   ```
   
3. 해설

   - 데이터가 최대힙의 최대값보다 작으면 최대힙에 추가
   - 최소힙과 최대힙의 길이가 2차이나면 하나 빼서 하나 넣는것으로 길이를 맞춘다.
   - 최소힙이 더 많으면 최소힙 출력, 아니면 최대힙 출력