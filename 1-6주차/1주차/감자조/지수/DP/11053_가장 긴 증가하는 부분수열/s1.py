import sys
sys.stdin = open('input.txt')

# 시간 복잡도 O(n^2)

N = int(input())
nums = list(map(int, input().split()))
counter = [1]*N

for i in range(1, N):
    for j in range(i):
        if nums[i] > nums[j]:
            counter[i] = max(counter[i], counter[j]+1)

print(counter)
print(max(counter))