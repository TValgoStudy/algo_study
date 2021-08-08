### 내 풀이

1. 이렇게 푼 이유?

   - set과 백트래킹으로 풀어보려고 했지만 틀림.. 그리고 백트래킹이나 DP이려면 현재 배운 알파벳으로 읽을 수 있는 단어의 수를 매번 세야하는데, 그게 더 오래 걸림
   - 블로그 참고하여 비트 연산으로 품! 이런 어느정도 범위가 정해진 것 안에서 특정 데이터가 포함됐냐 아니냐를 따지는데에는 비트 연산이 좋을 것 같음!
   - (중요) `^` 연산은 XOR, 둘중 하나만 1이어야 참으로 반환됨, 그래서 111...11 과 XOR 하면 원본 데이터를 뒤집는 기능을 함!!!!
   - (중요) 뒤집은 값(안 배운거에 1된 이진수)와 배울 단어를 `&`연산하면 `단어에 들어있는 알파벳 중 안배운 것`만 1이 됨
   - 따라서 위 값이 0이라는 건, 그 단어의 알파벳은 모두 다 배웠다는 의미로, 읽을 수 있는 것!!!

2. 실행시간

   - pypy 372ms / python 2276ms

3. 코드1

   ```python
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
                temp ^= (1 << 26) - 1 # 🧡 1, 0 뒤집기 
                answer = max(answer, sum(1 if (temp & a) == 0 else 0 for a in converted_word)) # 🧡
            print(answer)
   ```



### 다른 사람의 풀이

1. 실행시간

   - pypy 208ms (leedh2004) 

2. 코드

   ```python
    from itertools import combinations
    N, K = map(int, input().split())
    # a, n, t, i, c 는 기본적으로 배워야 함
    D = "antic"
    B = []
    for _ in range(N):
        s = input()
        if K < 5:
            print(0)
            exit(0)
        b = 0 
        for c in s:
            if c in D:
                continue
            diff = ord(c) - ord('a')
            if b & 1 << diff == 0:
                b = b | 1 << diff
        B.append(b)
    
    C = []
    for i in range(26):
        c = chr(i + ord('a'))
        if c in D:
            continue
        C.append(c)
    
    ans = 0
    for lis in combinations(C, K-5):
        C = 0 
        cand = 0
        for c in lis:
            C = C | 1 << ord(c) - ord('a')
        for b in B:
            if b & C == b:
                cand += 1
        ans = max(ans, cand)
    print(ans)

   ```

