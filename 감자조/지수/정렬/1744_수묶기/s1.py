import sys
sys.stdin = open('input.txt')

N = int(input())

plus = []
minus = []
one = 0 # 처음에 생각하지 못한 조건
zero = 0
result = 0

for _ in range(N):
    num = int(input())
    if num > 1:
        plus.append(num)
    elif num == 1:
        one += 1
    elif num == 0:
        zero += 1
    else:
        minus.append(num)

# 절대값이 큰순 ~ 작은순으로 정렬
plus.sort(reverse=True)
minus.sort()

P = len(plus)
M = len(minus)

# 큰수 두개씩 곱
for i in range(0, P//2):
    result += plus[2*i] * plus[2*i+1]

# 홀수개면 마지막것도 더하기
if P % 2:
    result += plus[-1]

# 음수도 두개 짝지어서 곱
for j in range(0, M//2):
    result += minus[2*j] * minus[2*j+1]

# 홀수개고, 0도 없으면 더해져야 함
if M % 2 and zero == 0:
    result += minus[-1]

result += one # 1은 곱한 것보다 더한게 큼 : 3*1 < 3+1

print(result)

