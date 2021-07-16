import sys
sys.stdin = open('input.txt')

# 폭발 연쇄 가능
# 남은 문자 리턴, 없을 경우 FRULA 리턴

# 스택 사용
# 896ms 성공!

text = input()
bomb = input()

T = len(text)
B = len(bomb)

stack = [''] * T
si = 0

for ti in range(T):
    stack[si] = text[ti]

    if si < B - 1:
        si += 1
        continue

    for ri in range(B):
        if stack[si-ri] != bomb[B-ri-1]:
            break
    else:
        si -= B

    si += 1

if si:
    print(''.join(stack[:si]))
else:
    print('FRULA')