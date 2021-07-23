from itertools import product
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
print(list(map(sum, product(*zip(*arr)))).count(0))