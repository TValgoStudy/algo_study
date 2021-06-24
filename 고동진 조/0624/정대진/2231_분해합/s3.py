N = int(input())
# 117 -> 99, 216 -> 198
weight = [10**i+1 for i in range(7)]
str_idx = '1'
while True:
    total = 0
    idx = 0
    while idx < len(str_idx):
        total += weight[idx] * int(str_idx[len(str_idx) - 1 - idx])
        idx += 1
    if total == N:
        print(str_idx)
        break
    tmp = int(str_idx)+1
    if tmp > N:
        break
    str_idx = str(tmp)

if total != N:
    print(0)
