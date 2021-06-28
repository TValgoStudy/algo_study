import sys
sys.stdin = open('eval_input.txt')
input = sys.stdin.readline

N = int(input())

# 1~99 -> N개 (원소가 1 or 2개뿐일때는 무조건)
# 100~999 : 공차가 |0| ~ |4| 까지 가능

hansu = []
for i in range(1, 10):
    for j in range(-4, 5):
        first = i
        second = first+j
        third = second+j
        nums = first*100 + second*10 + third
        if 0 <= first < 10 and 0 <= second < 10 and 0 <= third < 10 and 100 < nums < 1000:
            hansu.append(nums)
print(hansu)

result = 0
if N >= 100:
    result += 99
    for han in hansu:
        if han <= N:
            result += 1
        else:
            break

else:
    result = N

print(result)

