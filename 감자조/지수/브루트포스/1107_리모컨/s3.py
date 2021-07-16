import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

target = int(input())
N = int(input())
broken = list(map(int, input().split()))

button = [1] * 10
for b in broken:
    button[b] = 0


MIN = abs(target - 100)

for chanel in range(0, 1000001):
    for ch in str(chanel):
        if button[int(ch)] == 0:
            break
    else:
        MIN = min(MIN, len(str(chanel)) + abs(target - chanel))

print(MIN)

