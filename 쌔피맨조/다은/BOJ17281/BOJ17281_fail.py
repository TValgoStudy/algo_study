import sys
from pandas import DataFrame
sys.stdin = open('input.txt')

N = int(input())
IN = [list(map(int, input().split())) for _ in range(N)]

IN_trans = sorted([i for i in zip(*IN)])
IN_trans.sort(key = lambda x: (x.count(0)))

idx0 = IN_trans.pop(0)
IN_trans.insert(3, idx0)
IN_default = [i for i in zip(*IN_trans)]

print(DataFrame(IN_default))
out = 0
old_c, r, c = 0, 0, 0
score = 0
while r < N:
    cur = [0, 0, 0, 0]
    while out != 3:
        if IN_default[r][c] == 0:
            out += 1
            old_c = c
        else:
            for k in range(1, 4):
                if cur[k]:
                    if k + IN_default[r][c] >= 4:
                        cur[k] = 0
                        score += 1
                    else:
                        cur[k + IN_default[r][c]] = 1
            if IN_default[r][c] >= 4:
                score += 1
            else:
                cur[IN_default[r][c]] = 1

        c = c+1 if c != 8 else 0
    r += 1
    c = old_c
    c = c + 1 if c != 8 else 0
    out = 0
print(score)