# swea 1213_String
# 수업때 보이어 무어 했었던 것 (다시 보니까 잘못한 것 같다)

import sys
sys.stdin = open('input.txt', 'r', encoding='UTF-8')

for _ in range(10):
    tc = input()
    word = input()
    txt = input()
    skip = {}
    cnt = 0

# 보이어 무어
len_word = len(word)  # word의 길이
f_idx = len(word) - 1  # word의 마지막 인덱스
idx = len_word - 1  # txt에서 현재 비교하고 있는 인덱스

# 스킵 배열 생성
for i in range(len_word):
    skip[word[i]] = len_word - (i + 1)

while idx <= len(txt) - 1:
    # 만약 txt[idx]와 word의 마지막 글자가 동일하다면
    if txt[idx] == word[f_idx]:
        # txt[idx]앞쪽 글자들도 비교해줘야함.
        for i in range(len_word):
            # 만약 txt 앞쪽 글자가 다르면 for문을 break하고, 다음 idx로
            if txt[idx - i] != word[f_idx - i]:
                idx += len_word
                break
        # for문이 정상적으로 모두 돌았으면 존재하는 것.
        # +1 해주고, 다음 idx로 넘어가야하니까 +len_word. 여기서 break는 하면 while종료니까 X
        else:
            cnt += 1
            idx += len_word
    # 동일하지 않으면 skip 배열만큼 idx +
    else:
        idx += skip.get(txt[idx], len_word)
print("#{} {}".format(tc, cnt))


# 인덱싱
for _ in range(10):
    tc = input()
    word = input()
    txt = input()

cnt = 0
i = 0
while i + len(word) <= len(txt):
    if txt[i] == word[0]:
        ok = 0
        for j in range(len(word)):
            if txt[i + j] != word[j]:
                break
        else:
            cnt += 1
    i += 1

print("#{} {}".format(tc, cnt))