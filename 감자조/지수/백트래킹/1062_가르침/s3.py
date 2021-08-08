import sys
from itertools import combinations
sys.stdin = open('input.txt')
input = sys.stdin.readline


# a를 0, z를 25로 하는 ord 구하기
def get_ord(x):
    return ord(x) - ord('a')


# 각 알파벳의 이진수를 or 하여 전체 단어를 이진표기로 바꾸기
def convert(word):
    result = 0
    for w in word:
        result |= (1 << w)
    return result


n, k = map(int, input().split())
must = set([get_ord(a) for a in ['a', 'c', 'i', 'n', 't']])
base = 0 # must로 이루어진 이진값


# 'a', 'c', 'i', 'n', 't' 의 이진 표현
for i in must:
    base |= (1 << i)

words = [set(map(get_ord, input().strip())) for _ in range(n)] # 단어들 ord로 변환한 것
converted_word = [convert(word) for word in words] # 2진코드로 변환한 것

candidates = set().union(*words) - must # 가르쳐야할 모든 단어에서 must 제외한 것
answer = 0

if k < 5:
    print(0) # antic만 해도 5글자라서, 5개 이하면 아무것도 못 읽음
else:
    if len(candidates) <= (k - 5): # 가르쳐야 하는 것 <= 가르칠 수 있는 것 --> 다 읽을 수 있음
        print(n)
    else:
        for c in combinations(candidates, k - 5): # 후보군 조합 생성
            temp = base # 기본적으로 배운 antic
            for i in c:
                temp |= (1 << i) # 새로 배운 알바펫 or 연산으로 추가
            temp ^= (1 << 26) - 1 # 1, 0 뒤집기
            answer = max(answer, sum(1 if (temp & a) == 0 else 0 for a in converted_word)) # 🧡
        print(answer)