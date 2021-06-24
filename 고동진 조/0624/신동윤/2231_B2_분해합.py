N = int(input())
answer = 0
for i in range(1, N):
    total = i
    num = str(i)
    for j in num:
        total += int(j)

    if total == N:
        answer = i
        break

print(answer)



