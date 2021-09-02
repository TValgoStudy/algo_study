import sys
sys.stdin = open('input.txt')

def kmp(content):
    n = len(content)
    table = [0] * n
    j = 0
    for i in range(1, n): # target index 시작
        while j > 0 and content[i] != content[j]:
            j = table[j-1]

        if content[i] == content[j]:
            j += 1
            table[i] = j

    print(table)
    return table


L = int(sys.stdin.readline())
ad = sys.stdin.readline().rstrip()

print(L - kmp(ad)[-1])