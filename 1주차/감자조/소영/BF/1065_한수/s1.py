#
# def hansu(num):
#     cnt = 0
#     for i in range(1, num+1):
#         if 1 <= i <= 9: # 1~9까지는 무조건 한수
#             cnt += 1
#         elif 10 <= i <= 99: # 10~99 까지도 무조건 한수
#             cnt += 1
#         elif 100 <= i <= 999: # 100 ~ 999의 경우는 체크해봐야 한다
#             a = i // 100 # 첫자리
#             b = (i//10) - a*10 # 두번째 자리
#             c = i - a*100 - b*10 # 세번째 자리
#             if (a-b) == (b-c): # 가 등차면
#                 cnt +=1 # 카운트
#     print(cnt)

def hansu(num):
    cnt = 0
    if num < 100:
        return num
    elif num < 111:
        return 99
    else:
        for i in range(111, num+1):
            a = i // 100 # 첫자리
            b = (i//10) - a*10 # 두번째 자리
            c = i - a*100 - b*10 # 세번째 자리
            if (a-b) == (b-c): # 가 등차면
                cnt +=1 # 카운트
        return cnt + 99

num = int(input())
print(hansu(num))


# num = int(input())
# hansu(num)

print(hansu(110))
print(hansu(1))
print(hansu(210))
print(hansu(1000))
print(hansu(1))
