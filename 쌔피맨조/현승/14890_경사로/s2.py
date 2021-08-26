import sys
sys.stdin = open("input.txt", "r")
# input = sys.stdin.readline

N, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0

for i in range(N):
    h = arr[i][0]
    cnt = 1
    pre_dir = 0
    down_cnt = 0
    for j in range(1, N):
        if pre_dir == -1:
            down_cnt += 1
        # 평지
        if h == arr[i][j]:
            if pre_dir == -1:
                if j == N-1 and down_cnt < L:
                    break
                if down_cnt >= L:
                    down_cnt = 0
                    cnt = 1
            else:
                cnt += 1
        # 오르막
        elif h + 1 == arr[i][j]:
            if pre_dir == -1:
                if down_cnt < L:
                    break
                else:
                    down_cnt = 0
            if down_cnt == L:
                break
            if cnt < L:
                break
            pre_dir = 1
            down_cnt = 0
            cnt = 1
            h += 1
        # 내리막
        elif h - 1 == arr[i][j]:
            if j == N-1 and L > 1:
                break
            if pre_dir == -1:
                if down_cnt < L:
                    break
                else:
                    down_cnt = 0
            pre_dir = -1
            down_cnt = 0
            cnt = 1
            h -= 1
        # 높이차가 2 이상
        else:
            break
    else:
        print(i, '행')
        ans += 1


for i in range(N):
    h = arr[0][i]
    cnt = 1
    pre_dir = 0
    down_cnt = 0
    for j in range(1, N):
        # 평지
        if h == arr[j][i]:
            if pre_dir == -1:
                down_cnt += 1
                if j == N-1 and down_cnt < L:
                    break
                if down_cnt >= L:
                    down_cnt = 0
                    cnt = 1
            else:
                cnt += 1
        # 오르막
        elif h + 1 == arr[j][i]:
            if pre_dir == -1:
                if down_cnt < L:
                    break
                else:
                    down_cnt += 1
            if cnt < L:
                break
            pre_dir = 1
            down_cnt = 0
            cnt = 1
            h += 1
        # 내리막
        elif h - 1 == arr[j][i]:
            if j == N-1 and L > 1:
                break
            if pre_dir == -1:
                if down_cnt < L:
                    break
                else:
                    down_cnt = 0
            pre_dir = -1
            down_cnt = 0
            cnt = 1
            h -= 1
        # 높이차가 2 이상
        else:
            break
    else:
        print(i, '열')
        ans += 1

print(ans)