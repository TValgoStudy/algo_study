import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def isHansu(x):
    if (x < 100):
        return True
    elif ((x // 100 - (x % 100) // 10) == ((x % 100) // 10 - (x % 10))):
        return True
    else:
        return False


n = int(input())
cnt = 0
for i in range(1, n + 1):
    if isHansu(i):
        cnt += 1

print(cnt)