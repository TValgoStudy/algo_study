N = int(input())
cnt = 0
num = 665

while cnt < N:
    num += 1
    str_num = str(num)
    check = 0
    for digit in str_num:
        if digit == '6':
            check += 1
        else:
            check = 0
        if check == 3:
            cnt += 1
            break

print(num)
