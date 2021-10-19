import sys
sys.stdin = open('input.txt')

N = int(input())
cnt = 0
while N >= 0:
    if not N % 5:
        cnt += N // 5
        print(cnt)
        break
    else:
        N -= 3
        cnt += 1
else:
    print(-1)

# 함수로 작성하면 런타임 에러
# def find(N):
#     cnt = 0
#     while N >= 0:
#         if not N % 5:
#             cnt += N // 5
#             return cnt
#         else:
#             N -= 3
#             cnt += 1
#     return -1
# print(find(N))