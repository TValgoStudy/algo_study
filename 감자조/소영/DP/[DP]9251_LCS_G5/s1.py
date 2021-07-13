import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


f_string = list(input().rstrip())
s_string = list(input().rstrip())
f_len = len(f_string)
s_len = len(s_string)

dp = [[0] * (s_len+1) for _ in range(f_len+1)]
print(dp)

for i in range(1, f_len+1):
    for j in range(1, s_len+1):
        # 지금 확인하고 있는 첫 문자열의 값이 두번째 문자열의 값과 같으면
        if f_string[i-1] == s_string[j-1]:
            # 해당 자리는 전 자리일때보다 최장 길이가 하나 늘어난다! (직관적)
            dp[i][j] = dp[i - 1][j - 1] + 1
        # 같지 않다면
        else:
            # 두 문자열을 하나씩 따로 추가한 것 중에 큰거 써야함
            # 예시
            # # ABCD, ABDF
            # # i=2, j=2 까지는 공통 => dp[1][1]=1, dp[2][2]=2
            # # i=3, j=3 에서 어긋남
            # # 이때 i-1, j-1을 넣으면 dp[3][3] = 2, dp[4][4]=2 가 됨
            # # 따라서 ABC AB, AB ABD 를 비교해서 더 큰 값을 가져온다
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
print(dp)

print(dp[-1][-1])