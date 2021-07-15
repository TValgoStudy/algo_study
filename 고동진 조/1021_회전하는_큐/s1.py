# 첫째 줄에 큐의 크기 N과 뽑아내려고 하는 수의 개수 M
# N은 50보다 작거나 같은 자연수이고, M은 N보다 작거나 같은 자연수이다.
N, M = map(int, input().split())
# 지민이가 뽑아내려고 하는 수의 위치가 순서대로 주어진다. 위치는 1보다 크거나 같고, N보다 작거나 같은 자연수이다
arr = list(map(int, input().split()))

# 1. 첫 번째 원소를 뽑아낸다. 이 연산을 수행하면, 원래 큐의 원소가 a1, ..., ak이었던 것이 a2, ..., ak와 같이 된다.
# 2. 왼쪽으로 한 칸 이동시킨다. 이 연산을 수행하면, a1, ..., ak가 a2, .c.., ak, a1이 된다.
# 3. 오른쪽으로 한 칸 이동시킨다. 이 연산을 수행하면, a1, ..., ak가 ak, a1, ..., ak-1이 된다.
#  2번, 3번 연산의 최솟값을 출력하는 프로그램을 작성하시오.
# queue = [i for i in range(1, N+1)]
queue = [1] * N
ans = 0
idx = 0
for target in arr:
    right_idx = idx
    # go right
    right_cnt = 0
    while target != (right_idx+1):
        right_idx += 1
        if right_idx >= N:
            right_idx = 0
        if queue[right_idx]:
            right_cnt += 1
    # go left
    left_idx = idx
    left_cnt = 0
    while target != (left_idx+1):
        left_idx -= 1
        if left_idx < 0:
            left_idx = N-1
        if queue[left_idx]:
            left_cnt += 1

    if right_cnt <= left_cnt:
        ans += right_cnt
        idx = right_idx
    else:
        ans += left_cnt
        idx = left_idx
    queue[idx] = 0
    while not queue[idx] and sum(queue) != 0:
        idx += 1
        if idx >= N:
            idx = 0
print(ans)