import sys
sys.stdin = open('input.txt')

n = int(input())

node = list(list(map(int, input().split())) for _ in range(n-1))
print(node)

