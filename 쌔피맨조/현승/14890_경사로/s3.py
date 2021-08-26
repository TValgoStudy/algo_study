import sys
sys.stdin = open("input.txt", "r")
# input = sys.stdin.readline

def solution(my_arr):

    ret = 0
    for i in range(N):
        h = my_arr[i][0]
        down_cnt = 0
        pre_dir = 0
        up_cnt = 0
        for j in range(1, N):

            if pre_dir == -1:
                down_cnt += 1

                if j == N-1 and down_cnt < L:
                    break

                if down_cnt >= L:
                    pre_dir = 0
                    up_cnt = -1
                    down_cnt = 0
            else:
                up_cnt += 1

            diff = my_arr[i][j] - h
            if diff == 0:
                pass
            elif diff == 1:
                if pre_dir == -1 and down_cnt < L:
                    break
                if up_cnt < L:
                    break
                pre_dir = 1
                h += 1
                up_cnt = 0
                down_cnt = 0
            elif diff == -1:
                if pre_dir == -1 and down_cnt < L:
                    break
                pre_dir = -1
                h -= 1
                down_cnt = 1
                up_cnt = 0
            else:
                break
        else:
            ret += 1
    return ret

N, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
rotated_arr = []
for new in zip(*arr):
    rotated_arr.append(list(new))

print(solution(arr) + solution(rotated_arr))
