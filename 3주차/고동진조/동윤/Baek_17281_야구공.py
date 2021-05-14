import sys
sys.stdin = open("input.txt", "r")
import time
from itertools import permutations
'''
    안타: 1
    2루타: 2
    3루타: 3
    홈런: 4
    아웃: 0
'''
start = time.time()
N = int(input())
MAX = 0
records = []
for _ in range(N):
    records.append(list(map(int, input().split())))


for case in permutations(range(1, 9), 8):
    case = list(case)
    case.insert(3, 0)
    score = 0
    idx = 0


    for record in records:
        out_count = 0
        basement = [0, 0, 0]
        while out_count < 3:
            # 이분탐색, 트리 => 할 게 너무 많다. 내가 모든 세그먼트 트리 HDL, splay, 이진탐색트리, 부모과 자식.

            if idx == 9:
                idx -= 9

            hit = record[case[idx]]
            result = 0
            if hit == 1:
                result += basement[2]
                basement[2] = basement[1]
                basement[1] = basement[0]
                basement[0] = 1
            elif hit == 2:
                result += (basement[2] + basement[1])
                basement[2] = basement[0]
                basement[1] = 1
                basement[0] = 0
            elif hit == 3:
                result += (basement[2] + basement[1] + basement[0])
                basement[0], basement[1] = 0, 0
                basement[2] = 1
            elif hit == 4:
                result += (basement[2] + basement[1] + basement[0] + 1)
                basement[2] = 0
                basement[1] = 0
                basement[0] = 0
            else:
                out_count += 1

            score += result

            idx += 1

        MAX = max(MAX, score)

print(MAX)
print("time :", time.time() - start)

'''
1 2 4 3 0 2 1 0 3
1 2 1 2 0 0 0 0 1
3 4 2 3 1 2 3 4 0
0 1 2 3 4 2 1 0 0
0 0 0 0 0 0 1 4 4
0 4 0 4 0 4 0 4 0
0 4 2 2 2 2 2 2 2
1 1 1 1 1 1 1 1 0
0 2 0 3 0 1 0 2 0
'''







