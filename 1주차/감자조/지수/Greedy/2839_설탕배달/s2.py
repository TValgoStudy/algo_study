def solution(N):
    cnt = 0

    while N > 0:
        if N % 5 == 0:
            N -= 5
            cnt += 1
        elif N % 3 == 0:
            N -= 3
            cnt += 1
        elif N > 5:
            N -= 5
            cnt += 1
        else:
            return -1
    return cnt


print(solution(18))
print(solution(4))
print(solution(6))
print(solution(9))
print(solution(11))








