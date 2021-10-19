def solution(N):
    cnt5 = 0
    cnt3 = 0
    DP3 = [] # 3으로 나누어 떨어졌을때의 N과, 그때의 cnt5

    while N > 0:
        if N % 3 == 0: # 3으로 나누어 떨어지면 DP3에 담기
            DP3.append([N, cnt5]) # 돌아가기 위해 저장함

        if N >= 5: # 5이상이면 5로 빼고 다음으로
            N -= 5
            cnt5 += 1
        elif N % 3 == 0: # 3일때 딱 나누어 떨어져서 끝
            cnt3 += 1
            N -= 3
        else: # 1,2,4 인경우(5이상도 아니고, 3도 아니라서)
            if DP3: # 과거에 3으로 나누어 떨어진 적이 있었다면
                N, cnt5 = DP3.pop() # 그랬던 가장 최근 과거로 돌아간다.
                cnt3 += 1
                N -= 3
            else: # 몇번이나 돌아가 봤지만 or 애초부터 1,2,4가 들어왔다면
                return -1 # 더이상 돌아갈 수도 없고, 불가능 하니까 -1


    return cnt5+cnt3

print(solution(18))
print(solution(4))
print(solution(6))
print(solution(9))
print(solution(11))








