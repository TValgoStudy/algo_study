# https://bowbowbow.tistory.com/6#comment5168448
# https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm

def fail_function(W:str)->list:
    Pi = [0] * len(W)
    Pi[0] = -1
    j = 0
    for i in range(1, len(W)-1):
        while j > 0 and W[i] != W[j]:
            j = Pi[j]
        if W[i] == W[j]:
            j += 1
            Pi[i+1] = j
    return Pi

fail_function('ABC ABCDAB ABCDABCDABDE')

def KMP(pat:str, txt:str)->list:
    pi = fail_function(pat)    # pi: pat 실패함수

    n, m = len(txt), len(pat)  # n: txt 길이, m: pat 길이
    i, j = 0, 0                # i: txt's idx, j: pat's idx

    ans = []                   # 어느 인덱스에서 답이 나오는지
    while i < n:
        if txt[i] == pat[j]:     # i, j인덱스 글자가 같으면
            i += 1               # i, j 1씩 증가시켜서
            j += 1               # 다음 글자를 비교하러 가기
            if j == m:           # pat을 찾았으면
                ans.append(i-j)  # ans에 추가하고
                j = 0            # 다음을 위해 0으로 만들어주기
        else:
            j = pi[j]          # j를 실패함수 값으로
            if j < 0:          # j가 0이면 (-1)
                i += 1         # i, j 1씩 올려주기
                j += 1
    # print(ans)
    return ans

KMP('ABCDABD', 'ABC ABCDAB ABCDABCDABDE')