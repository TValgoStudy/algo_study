import sys
sys.stdin = open('input.txt')

def main():
    string = input().strip()
    bomb = input().strip()
    bombl = list(bomb)
    b_last = bomb[-1]
    bl = len(bomb)

    ans = []
    for l in string:
        ans.append(l)
        if b_last == l and bombl == ans[-bl:]:
            del ans[-bl:]

    print(''.join(ans) if ans else "FRULA")


if __name__ == '__main__':
    main()
