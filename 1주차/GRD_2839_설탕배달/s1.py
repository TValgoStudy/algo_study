def sweet(kg):
    cnt_5 = kg//5
    cnt_3 = 0

    if kg%5 == 0:
        return cnt_5

    else:
        total = cnt_5*5 + 5
        cnt_5 += 1
        for i in range(3):
            if total >= 5:
                cnt_5 -= 1
                total -= 5
                for j in range(1,5):
                    if total + 3*j == kg:
                        cnt_3 += j
                        return cnt_5 + cnt_3
                    elif total + 3*j > kg:
                            break
    return -1




kg = int(input())
print(sweet(kg))

print(sweet(18))
print(sweet(4))
print(sweet(6))
print(sweet(9))
print(sweet(11))
print(sweet(30))