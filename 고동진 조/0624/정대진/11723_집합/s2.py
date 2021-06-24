M = int(input())
S = set()
for _ in range(M):
    command = input()
    # all: S를 {1, 2, ..., 20} 으로 바꾼다.
    if command == 'all':
        S = set(range(1, 21))
    elif command == 'empty':
        # empty: S를 공집합으로 바꾼다.
        S = set()
    else:
        operator, el = command.split()
        el = int(el)
        # add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
        if operator == 'add':
            S.add(el)
        # remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
        elif operator == 'remove':
            if el in S:
                S.remove(el)
        # check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
        elif operator == 'check':
            print(int(el in S))
        # toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
        else:
            if el in S:
                S.remove(el)
            else:
                S.add(el)
