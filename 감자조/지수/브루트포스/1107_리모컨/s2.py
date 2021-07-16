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

T = len(target)
MIN = 987564321

def pushButton(idx, num):
    global MIN

    if idx == T:
        MIN = min(MIN, abs(int(num) - int(target)))
        return

    if broken[int(target[idx])] == 0:
        pushButton(idx+1, num + target[idx])
    else:
        for i in range(1, 10):
            x = int(target[idx]) + i
            if x > 9: x = 0
            if broken[x] == 0:
                pushButton(idx + 1, num + str(x))
                break

        for i in range(1, 10):
            x = int(target[idx]) - i
            if x < 0: x = 9
            if broken[x] == 0:
                pushButton(idx + 1, num + str(x))
                break



pushButton(0, '')

print(min(MIN + T, abs(int(target) - 100)))

