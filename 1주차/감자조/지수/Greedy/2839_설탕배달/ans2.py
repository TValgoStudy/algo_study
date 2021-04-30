import sys
sys.stdin = open('input.txt')

N = int(input())

cnt = 0
while True:
    if N % 5 == 0: # 5로 완전히 나누어 떨어지지 않는 경우는
        cnt += (N//5) # 완전히 나누어 떨어지면 횟수 더해서 출력
        print(cnt)
        break
    N -= 3 # 3 빼고 다시 반복
    cnt += 1
    if N < 0:
        print(-1)
        break