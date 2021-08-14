import sys
sys.stdin = open('input.txt')


# 어떤 수의 합을 연속된 소수로 만들기 위해서
# 1~n 사이에서 소수를 구한다
# s,e를 모두 0으로 하여 시작한다
# 구간합이 n보다 작으면 e += 1
# 구간합이 n보다 크면 s += 1
# s > e가 되거나 e > 길이이면 종료


def solution():
    n = int(sys.stdin.readline())
    prime = findPrime(n)

    s, e = 0, 0
    l = len(prime)
    ans = 0

    while s <= e and e < l:
        total = sum(prime[s:e+1])
        if total ==  n:
            ans += 1
            e += 1
        elif total < n:
            e += 1
        else:
            s += 1

    return ans



def findPrime(n):
    arr = [1] * (n+1) # 에라토스테네스의 체
    arr[0], arr[1]  = 0, 0 # 0, 1 소수 아님

    for i in range(2, int(n**0.5) + 1):
        for k in range(2, n//i+1):
            arr[i*k] = 0 # 어떤 수의 배수로 표현되면 소수 아님

    prime = []
    for i in range(n+1):
        if arr[i]:
            prime.append(i)

    return prime


print(solution())
