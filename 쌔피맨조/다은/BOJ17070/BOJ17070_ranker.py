import sys
from pandas import DataFrame
sys.stdin = open('input.txt')

N = int(input())
maps = [list(map(int, input().split())) for _ in range(N)]

table = [[[0]*3 for _ in range(N)] for _ in range(N)]
table[0][1][0] = 1

for x in range(2, N):
    if maps[0][x] == 0:
        table[0][x][0] = table[0][x-1][0]

for y in range(N):
    for x in range(2, N):
        if maps[y][x] == maps[y][x-1] == maps[y-1][x] == 0:
            table[y][x][2] = table[y-1][x-1][0] + table[y-1][x-1][1] + table[y-1][x-1][2]
        if maps[y][x] == 0:
            table[y][x][0] = table[y][x-1][2] + table[y][x-1][0]
            table[y][x][1] = table[y-1][x][2] + table[y-1][x][1]

print(sum(table[-1][-1]))