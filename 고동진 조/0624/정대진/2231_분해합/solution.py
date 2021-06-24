N = int(input())
temp = N
start_num = max(0, N - 9*len(str(N)))

for i in range(start_num, N):
    if i + sum(map(int, str(i))) == N:
        print(i)
        break
else:
    print(0)