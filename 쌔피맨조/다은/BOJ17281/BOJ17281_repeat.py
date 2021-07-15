import sys
from itertools import permutations
# sys.stdin = open('input.txt')

# 이걸로 하면 788ms
N = int(input())
IN = [list(map(int, input().split())) for _ in range(N)]
# 이걸로 하면 760ms
# N = int(sys.stdin.readline())
# IN = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

people = [1, 2, 3, 4, 5, 6, 7, 8]
result = 0
for turn in permutations(people, 8):
    turn = list(turn)  # permutations object이므로 list로 만들어 준다.
    turn.insert(3, 0)  # 인덱스 3에 0을 넣기
    score, idx = 0, 0
    for inning_score in IN:
        out = 0
        a, b, c = 0, 0, 0
        while out < 3:
            # 아웃일 때
            if inning_score[turn[idx]] == 0:
                out += 1
            # 1이면 base3 인 c가 들어온다.
            # score에 숫자가 아니라 a,b,c를 더해주는 이유는
            # a, b, c에 사람이 있을수도 없을수도(1, 0) 있기 때문
            elif inning_score[turn[idx]] == 1:
                score += c
                a, b, c = 1, a, b
            # 2이면 base2, 3인 b, c가 들어온다
            elif inning_score[turn[idx]] == 2:
                score += (b+c)
                a, b, c = 0, 1, a
            # 3이면 base1, 2, 3 인 a, b, c가 들어온다.
            elif inning_score[turn[idx]] == 3:
                score += (a+b+c)
                a, b, c = 0, 0, 1
            # 4이면 base1, 2, 3, 4인 a, b, c + 타자가 들어온다
            elif inning_score[turn[idx]] == 4:
                score += (a+b+c+1)
                a, b, c = 0, 0, 0
            # 9이면 0이고, 이하면 +1을 이렇게 표현할 수 있다!
            idx = (idx+1) % 9
    result = max(result, score)
print(result)



