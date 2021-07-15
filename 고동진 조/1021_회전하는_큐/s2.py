from collections import deque
N, M = map(int, input().split())
arr = list(map(int, input().split()))
nums = [i for i in range(1, N+1)]
deq = deque(nums)
ans = 0
for target in arr:
    for idx in range(len(deq)):
        if deq[idx] == target:
            break
    if idx <= len(deq) // 2:
        ans += idx
        deq.rotate(-idx)
    else:
        tmp = len(deq) - idx
        ans += tmp
        deq.rotate(tmp)
    deq.popleft()
print(ans)

