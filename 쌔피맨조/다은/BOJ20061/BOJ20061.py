import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame


def func(t, red, green):
    global result

    block = []
    for r in range(4):
        for c in range(4):
            if red[r][c]:
                block.append((r, c))

    a1, b1 = block.pop()
    if t == 1:
        for r in range(7):
            if r > 5 or green[r][b1]:
                target_r = r - 1
                break
        green[target_r][b1] = 1
    elif t == 2:
        a2, b2 = block.pop()
        for r in range(7):
            if r > 5 or (green[r][b1] or green[r][b2]):
                target_r = r - 1
                break
        green[target_r][b1] = 1
        green[target_r][b2] = 1
    else:
        a2, b2 = block.pop()
        for r in range(7):
            if r > 5 or green[r][b1]:
                target_r = r - 1
                break
        green[target_r][b1] = 1
        green[target_r-1][b1] = 1

    # 블록 4개 1줄 터뜨릴 때
    remove = []
    for r in range(6):
        if sum(green[r]) == 4:
            remove.append(r)
    # 뒷부분부터 pop하려고 sort
    remove.sort()
    result += len(remove)
    # 새로운 행 만들기
    add_row = [[0]*4 for _ in range(len(remove))]
    # 제거해야하는 행 pop해주기
    while remove:
        r = remove.pop()
        green.pop(r)
    green = add_row + green

    # 0, 1 행에 무언가 있어서 내려갈 때
    remove = []
    for r in range(2):
        if sum(green[r]) > 0:
            remove.append(r)
    add_row = [[0] * 4 for _ in range(len(remove))]
    while remove:
        remove.pop()
        green.pop()
    green = add_row + green

    return green






N = int(input())

blue = [[0]*4 for _ in range(6)]
green = [[0]*4 for _ in range(6)]
result = 0

for _ in range(N):
    red = [[0] * 4 for _ in range(4)]
    t, x, y = map(int, input().split())
    if t == 1:
        red[x][y] = 1
    elif t == 2:
        red[x][y] = 1
        red[x][y+1] = 1
    else:
        red[x][y] = 1
        red[x+1][y] = 1

    green = func(t, red, green)

    if t == 2:   t = 3
    elif t == 3: t = 2
    red_cc = [i for i in zip(*red[::-1])]
    blue = func(t, red_cc, blue)




print(result)
tile = 0
for r in range(6):
    tile += sum(green[r])
    tile += sum(blue[r])
print(tile)
