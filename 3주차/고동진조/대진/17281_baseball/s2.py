import sys
from itertools import permutations


if __name__ == "__main__":
    n = int(sys.stdin.readline())  # 이닝 수
    data = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

    people = [1, 2, 3, 4, 5, 6, 7, 8]
    answer = 0
    for turn in permutations(people, 8):
        turn = list(turn)
        turn = turn[:3] + [0] + turn[3:]
        score = 0
        index = 0
        for inning in range(1, n + 1):
            out_cnt = 0  # 아웃 카운트
            status = [0, 0, 0]
            base_1, base_2, base_3 = 0, 0, 0  # 1, 2, 3루 주자
            while out_cnt < 3:
                if data[inning - 1][turn[index]] == 0:
                    out_cnt += 1
                elif data[inning - 1][turn[index]] == 1:
                    score += base_3
                    base_1, base_2, base_3 = 1, base_1, base_2
                elif data[inning - 1][turn[index]] == 2:
                    score += (base_2 + base_3)
                    base_1, base_2, base_3 = 0, 1, base_1
                elif data[inning - 1][turn[index]] == 3:
                    score += (base_1 + base_2 + base_3)
                    base_1, base_2, base_3 = 0, 0, 1
                elif data[inning - 1][turn[index]] == 4:
                    score += (base_1 + base_2 + base_3 + 1)
                    base_1, base_2, base_3 = 0, 0, 0
                # index = (index + 1) % 9
                index += 1
                if index == 9:
                    index = 0
        answer = max(answer, score)  # (타자 순서, 현재 타자 번호, 득점)
    print(answer)