A = input()
B = input()

DP = [0 for _ in range(1000)]
memo = ['' for _ in range(1000)]
answer = ''
for i in range(len(A)):
    max_val = 0
    max_idx = 0
    for j in range(len(B)):
        if max_val < DP[j]:
            max_val = DP[j]
            max_idx = j
        elif A[i] == B[j]:
            DP[j] = max_val + 1
            if len(memo[max_idx]):
                temp = memo[max_idx] + B[j]
                memo[j] = temp
                if len(answer) < len(memo[j]):
                    answer = temp
            else:
                memo[j] = B[j]

print(max(DP))
if answer:
    print(answer)