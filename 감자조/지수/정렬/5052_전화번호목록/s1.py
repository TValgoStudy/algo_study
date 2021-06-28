import sys
sys.stdin = open('eval_input.txt')
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    phone_book = [0] * N
    for i in range(N):
        phone_book[i] = input().strip()
    phone_book.sort()
    # print(phone_book)
    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            print('NO')
            break
    else:
        print('YES')