import sys
sys.stdin = open('input.txt')

# 모든 단어는 "anta"로 시작되고, "tica"로 끝난다.
# 즉, a/c/n/t/i 는 무조건 알아야 된다.
# K가 5보다 작으면 읽을 수 있는게 하나도 없다.

N, K = map(int, sys.stdin.readline().split())
C = K - 5 # a/c/n/t/i 제외하고 가르칠 수 있는 알파벳 수

words = []
T = set() # a/c/n/t/i 제외하고 가르쳐야할 전체 알파벳

antatica = ['a', 'c', 'n', 't', 'i']
visited = {chr(i): 0 for i in range(ord('a'), ord('z')+1)}

DP = [0] * (C+1)
MAX = 0

def init():
    global T
    for anta in antatica:
        visited[anta] = 1

    for _ in range(N):
        word = sys.stdin.readline()
        temp = set()
        for i in range(4, len(word) - 4):
            if word[i] not in antatica:
                temp.add(word[i])
        words.append(temp)
        T = T.union(temp)

    T = list(T)


def solution():
    if K < 5:
        return 0

    if K == 26:
        return N

    if not T:
        return N

    teach(0, 0)

    if DP:
        return max(DP)

    return 0


def teach(teachCnt, idx):

    if teachCnt > C:
        return

    readable = findCanRead()
    if readable < DP[teachCnt]:
        return

    DP[teachCnt] = readable

    for i in range(idx, len(T)):
        t = T[i]
        if visited[t]: continue # 이미 배운 단어 스킵

        visited[t] = 1
        teach(teachCnt + 1, i+1)
        visited[t] = 0


def findCanRead():
    learned = set()
    for alpha in visited.keys():
        if visited[alpha]:
            learned.add(alpha)

    ans = 0
    for word in words:
        if not (word - learned):
            ans += 1

    return ans

init()
print(solution())