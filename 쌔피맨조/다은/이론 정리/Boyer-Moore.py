# https://ee-22-joo.tistory.com/8
# https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_string-search_algorithm
# 위키에 있는 코드인데 모르겠다;

from typing import *

ALPHABET_SIZE = 26

def alphabet_index(c: str) -> int:
    val = ord(c.lower()) - ord("a")
    assert val >= 0 and val < ALPHABET_SIZE
    return val

# fundamental_preprocess에 쓰이는 함수
def match_length(S: str, idx1: int, idx2: int) -> int:
    if idx1 == idx2:
        return len(S) - idx1
    match_count = 0
    while idx1 < len(S) and idx2 < len(S) and S[idx1] == S[idx2]:
        match_count += 1
        idx1 += 1
        idx2 += 1
    return match_count

# good_suffix_table & full_shift_table 에 쓰이는 함수
def fundamental_preprocess(S: str) -> List[int]:
    if len(S) == 0:  # Handles case of empty string
        return []
    if len(S) == 1:  # Handles case of single-character string
        return [1]
    z = [0 for x in S]
    z[0] = len(S)
    z[1] = match_length(S, 0, 1)
    for i in range(2, 1 + z[1]):  # Optimization from exercise 1-5
        z[i] = z[1] - i + 1
    # Defines lower and upper limits of z-box
    l = 0
    r = 0
    for i in range(2 + z[1], len(S)):
        if i <= r:  # i falls within existing z-box
            k = i - l
            b = z[k]
            a = r - i + 1
            if b < a:  # b ends within existing z-box
                z[i] = b
            else:  # b ends at or after the end of the z-box, we need to do an explicit match to the right of the z-box
                z[i] = a + match_length(S, a, r + 1)
                l = i
                r = i + z[i] - 1
        else:  # i does not reside within existing z-box
            z[i] = match_length(S, 0, i)
            if z[i] > 0:
                l = i
                r = i + z[i] - 1
    return z

################# skip table 생성 #################

def bad_character_table(S: str) -> List[List[int]]:
    if len(S) == 0:
        return [[] for a in range(ALPHABET_SIZE)]
    R = [[-1] for a in range(ALPHABET_SIZE)]
    alpha = [-1 for a in range(ALPHABET_SIZE)]
    for i, c in enumerate(S):
        alpha[alphabet_index(c)] = i
        for j, a in enumerate(alpha):
            R[j].append(a)
    return R

def good_suffix_table(S: str) -> List[int]:
    L = [-1 for c in S]
    N = fundamental_preprocess(S[::-1])  # S[::-1] reverses S
    N.reverse()
    for j in range(0, len(S) - 1):
        i = len(S) - N[j]
        if i != len(S):
            L[i] = j
    return L

# 이건 무슨 함수지..?
def full_shift_table(S: str) -> List[int]:
    F = [0 for c in S]
    Z = fundamental_preprocess(S)
    longest = 0
    for i, zv in enumerate(reversed(Z)):
        longest = max(zv, longest) if zv == i + 1 else longest
        F[-i - 1] = longest
    return F



################# Boyer-Moore 알고리즘 #################
def string_search(P, T) -> List[int]:
    if len(P) == 0 or len(T) == 0 or len(T) < len(P):
        return []

    matches = []

    # Preprocessing
    R = bad_character_table(P)
    L = good_suffix_table(P)
    F = full_shift_table(P)

    k = len(P) - 1      # Represents alignment of end of P relative to T
    previous_k = -1     # Represents alignment in previous phase (Galil's rule)
    while k < len(T):
        i = len(P) - 1  # Character to compare in P
        h = k           # Character to compare in T
        while i >= 0 and h > previous_k and P[i] == T[h]:  # Matches starting from end of P
            i -= 1
            h -= 1
        if i == -1 or h == previous_k:  # Match has been found (Galil's rule)
            matches.append(k - len(P) + 1)
            k += len(P) - F[1] if len(P) > 1 else 1
        else:  # No match, shift by max of bad character and good suffix rules
            char_shift = i - R[alphabet_index(T[h])][i]
            if i + 1 == len(P):  # Mismatch happened on first attempt
                suffix_shift = 1
            elif L[i + 1] == -1:  # Matched suffix does not appear anywhere in P
                suffix_shift = len(P) - F[i + 1]
            else:               # Matched suffix appears in P
                suffix_shift = len(P) - 1 - L[i + 1]
            shift = max(char_shift, suffix_shift)
            previous_k = k if shift >= i + 1 else previous_k  # Galil's rule
            k += shift
    return matches
