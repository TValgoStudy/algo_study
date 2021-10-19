import sys
sys.stdin = open("input.txt", "r")
import time
start = time.time()

def permutation(idx ,cnt, score):
    global max_score
    if idx == 9:
        max_score = max(max_score, score)

    for i in range(idx, 9):
        if i == 3 or idx == 3:
            continue
        orders[i], orders[idx] = orders[idx], orders[i]
        permutation(i, )


N = int(input())
# 이닝
turns = [list(map(int, input().split())) for _ in range(N)]
# 0 ~ 8번 타자 순서
orders = [1, 2, 3, 0, 4, 5, 6, 7, 8]

max_score = 0
permutation(0, 0, 0)

print(max_score)
print("time: ", time.time() - start)