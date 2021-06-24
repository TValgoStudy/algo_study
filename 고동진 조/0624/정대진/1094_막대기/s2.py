X = int(input())
cnt = 0
for i in range(7):
    if X & 1 << i:
        cnt += 1
print(cnt)