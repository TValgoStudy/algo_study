def solution(cnt: int):
    if sum(stick) == X:
        return cnt

    if sum(stick) > X:
        stick.sort(reverse=True)
        a = stick.pop()
        a //= 2
        b = a

        stick.append(a)
        if sum(stick) >= X:
            return solution(cnt)
        else:
            stick.append(b)
            return solution(cnt + 1)


X = int(input())
stick = [64]
answer = solution(1)
print(answer)

