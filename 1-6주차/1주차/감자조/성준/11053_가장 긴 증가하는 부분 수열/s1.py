import sys
sys.stdin = open('input.txt')

N = int(input())

A = list(map(int, input().split()))

d=[1] * N
for i in range(1, N):
  for j in range(i):
    if A[j] < A[i]:
      d[i] = max(d[i], d[j] + 1)
# print(d)
print(max(d))

# 런타임 에러
# result = 0
# for i in range(len(A)):
#     mini = 0
#     cnt = 0
#     for j in range(i, len(A)):
#         if A[j] > mini:
#             cnt +=1
#             mini = A[j]
#     if result < cnt:
#         result = cnt
# print(result)