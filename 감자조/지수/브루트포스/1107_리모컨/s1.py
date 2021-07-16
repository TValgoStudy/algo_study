import sys
sys.stdin = open('input.txt')

# 0~9, +, -
# 0채널에서 - 누르면 변화 X
# 일부 버튼이 고장 났을때, N 채널에 가기 위한 최소 이동 횟수
# 싸피에서 준 고장난 계산기랑 비슷한듯
# 현재 채널은 100번이다.

target = input()
B = int(input())
broken = [0] * 10
for n in list(map(int, input().split())):
    broken[n] = 1

number = ''
T = len(target)



for t in target:
    if broken[int(t)] == 0:
        number += t
    else:
        i = 1
        while True:
            if int(t) + i < 10 and broken[int(t) + i] == 0:
                number += str(int(t) + i)
                break

            if int(t) - i > 0 and broken[int(t) - i] == 0:
                number += str(int(t) - i)
                break

            i += 1

ans1 = T + abs(int(number)-int(target))
ans2 = abs(int(target)-100)

print(min(ans1, ans2))


