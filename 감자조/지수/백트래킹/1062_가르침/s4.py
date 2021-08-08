import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# 2276

def get_ord(x):
    return ord(x) - ord('a')


def convert(word):
    result = 0
    for w in word:
        result |= (1 << w)
    return result


def teach(cnt, idx, word, readable):

    if readable < DP[cnt]:
        return
    DP[cnt] = readable

    if cnt >= k - 5:
        return

    for i in range(idx, len(candidates)):
        word |= (1 << candidates[i])
        temp = word ^ (1 << 26) - 1
        readable =  sum(1 if (temp & cvw) == 0 else 0 for cvw in converted_word)
        teach(cnt + 1, idx + 1, word, readable)
        word ^= (1 << candidates[i])


def solution():
    if k < 5:
        return 0

    if len(candidates) <= k - 5:
        return n

    teach(0, 0, base, 0)

    if DP:
        return max(DP)

    return 0


n, k = map(int, input().split())
must = set([get_ord(a) for a in ['a', 'c', 'i', 'n', 't']])
base = 0 # must로 이루어진 이진값

for i in must:
    base |= (1 << i)

words = [set(map(get_ord, input().strip())) for _ in range(n)] # 단어들 ord로 변환한 것
converted_word = [convert(word) for word in words] # 2진코드로 변환한 것

candidates = list(set().union(*words) - must) # 가르쳐야할 모든 단어에서 must 제외한 것

DP = [0] * (k - 4)
MAX = 0

print(solution())
