import sys
sys.stdin = open('input.txt')

# 폭발 연쇄 가능
# 남은 문자 리턴, 없을 경우 FRULA 리턴

# 너무 직관적이고 시간초과

s = input()
bomb = input()


while bomb in s:
    s = s.replace(bomb, '')

if s:
    print(s)
else:
    print('FRULA')