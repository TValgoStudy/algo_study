import sys
sys.stdin = open('input.txt')
q = lambda : map(int, sys.stdin.readline().split())

# 168ms
# 포인터 s,e 사용
# 구간합이 S보다 작으면 e + 1
# 구간합이 S보다 크면 MIN 갱신, s + 1


N, S = q()
nums = list(q())

s, e = 0, 0
total = nums[0]

MIN = 900000000

while s < N:

    if total >= S:
        MIN = min(MIN, e-s+1)

    elif e < N-1:
        e += 1
        total += nums[e]
        continue

    total -= nums[s]
    s += 1

if MIN == 900000000:
    print(0)
else:
    print(MIN)

