
# N = int(input())
# arr = list(map(int, input().split()))
N = 6
arr = [10, 20, 10, 30, 20, 50]

def longlong(idx):
    global stack
    global my_max
    if idx == N-1:
        if my_max < len(stack):
            my_max = len(stack)
            return

    if len(stack) + (N - idx -1 )< my_max:
        return

    for i in range(idx+1, N):
        if arr[i] > arr[stack[-1]]:
            stack.append(i)
            longlong(i)
            stack.pop()


stack = [0]
my_max = 0

for idx in range(N):
    if (N-idx) < my_max:
        break
    longlong(idx)

print(my_max)