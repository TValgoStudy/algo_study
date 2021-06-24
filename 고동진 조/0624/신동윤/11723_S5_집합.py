import sys
input = sys.stdin.readline

M = int(input())
S = [0 for _ in range(21)]

for _ in range(M):
    command = input().split()

    if len(command) == 2:
        option, num = command
    else:
        option = command[0]

    if option == 'add':
        S[int(num)] = 1
    elif option == 'remove':
        S[int(num)] = 0
    elif option == 'all':
        S = [1 for _ in range(21)]
    elif option == 'empty':
        S = [0 for _ in range(21)]
    elif option == 'toggle':
        if S[int(num)]:
            S[int(num)] = 0
        else:
            S[int(num)] = 1
    elif option == 'check':
        if S[int(num)]:
            print(1)
        else:
            print(0)
