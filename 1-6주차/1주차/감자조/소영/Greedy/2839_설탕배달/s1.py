def sweet(kg):
    cnt_5 = kg//5 # 5kg 수를 5로 나눈 몫으로 초기화
    cnt_3 = 0

    if kg%5 == 0: # 나누어 떨어지면
        return cnt_5 # cnt_5가 최소 수

    else: # 안나눠 떨어지면
        total = cnt_5*5 + 5 # 5kg 하나 증가 (반복문 초기 조건 통일)
        cnt_5 += 1
        for i in range(3): # 0~2 -> 3과 5의 최소공배수가 15이므로 2 (5*2=10) 까지만 빼서 경우의 수를 본다
            if total >= 5:  # 전체가 5 이상이면
                cnt_5 -= 1 # 5kg 하나 감소
                total -= 5
                for j in range(1, 5): # 1~4, j 만큼 3kg 추가 -> 3과 5의 최소공배수가 15이므로 4까지만
                    if total + 3*j == kg: # 더한 최종 무게가 목표와 같으면
                        cnt_3 += j # 개수 카운트하고
                        return cnt_5 + cnt_3 # 리턴
                    elif total + 3*j > kg: # 더한 최종 무게가 목표보다 커지면 현재의 cnt_5 수로는 조합을 찾을수 없다
                            break # 따라서 break, 첫번째 for문으로 돌아가서 cnt_5를 하나 더 뺀다
    return -1




kg = int(input())
print(sweet(kg))

print(sweet(18))
print(sweet(4))
print(sweet(6))
print(sweet(9))
print(sweet(11))
print(sweet(30))