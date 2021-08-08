import sys
import heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())

maxHeap = []
minHeap = []

for n in range(N):
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