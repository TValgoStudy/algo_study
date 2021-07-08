factorial_memo = [1]
T = int(input())
# 리스트를 해당하는 크기를 미리 생성하고 하자
# append는 O(1)이지만 일정 크기를 넘어서면 리스트 전체를 복사를 한 뒤에 시작을 함으로 O(N)이 된다.
for _ in range(T):
    N, M = map(int, input().split())
    # M C(combination) N = M!/(N! * (M - N)!) -> memoization
    while M >= len(factorial_memo):
        factorial_memo.append(factorial_memo[-1] * len(factorial_memo))
    print(factorial_memo[M]//(factorial_memo[N] * factorial_memo[M - N]))
