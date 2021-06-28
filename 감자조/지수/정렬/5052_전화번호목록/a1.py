import sys
sys.stdin = open('eval_input.txt')
r = sys.stdin.readline

def solve(book):
    for p1, p2 in zip(book, book[1:]):
        if p2.startswith(p1):
            return False
    return True

T = int(r())
for _ in range(T):
    N = int(r())
    flag = True
    book = []
    for _ in range(N):
        book.append(r().strip())

    book.sort()
    if solve(book):
        print("YES")
    else:
        print("NO")