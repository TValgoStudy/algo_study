
def hansu(num):
    cnt = 0
    for i in range(1, num+1):
        if 1 <= i <= 9:
            cnt += 1
        elif 10 <= i <= 99:
            cnt += 1
        elif 100 <= i <= 999:
            a = i // 100
            b = (i//10) - a*10
            c = i - a*100 - b*10
            if (a-b) == (b-c):
                cnt +=1
    print(cnt)

num = int(input())
hansu(num)
#
# hansu(110)
# hansu(1)
# hansu(210)
# hansu(1000)
# hansu(1)
