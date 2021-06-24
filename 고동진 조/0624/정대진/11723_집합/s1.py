M = int(input())
set_arr = [0]*21

for _ in range(M):
    command = input()
    # all: S를 {1, 2, ..., 20} 으로 바꾼다.
    if command == 'all':
        set_arr = [1]*21
    elif command == 'empty':
        # empty: S를 공집합으로 바꾼다.
        set_arr = [0]*21
    else:
        operator, el = command.split()
        # add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
        if operator == 'add':
            set_arr[int(el)] = 1
        # remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
        elif operator == 'remove':
            set_arr[int(el)] = 0
        # check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
        elif operator == 'check':
            print(set_arr[int(el)])
        # toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
        else:
            num = int(el)
            set_arr[num] = 0 if set_arr[num] else 1
