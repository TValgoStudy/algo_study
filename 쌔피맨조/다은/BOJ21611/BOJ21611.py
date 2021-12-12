import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def marble_destory(d, s, matrix):
    shark_r, shark_c = shark

    # d 방향 이동하며 구슬 없애기
    for k in range(1, s+1):
        nr = shark_r + dr[d] * k
        nc = shark_c + dc[d] * k
        if 0 <= nr < N and 0 <= nc < N:
            matrix[nr][nc] = -2

    # 한 줄로 표현 (구슬 없는 곳은 제외)
    array = matrix_to_array(matrix)
    start, bomb_flag = 1, 0

    while start or bomb_flag:
        start, bomb_flag = 0, 0

        # 구슬 폭발 => 4개이상 연속 구슬이면 없애기
        bomb_list = [-99]
        for idx in range(len(array)-1, -1, -1):
            # 기존 값이랑 동일하면 추가
            if bomb_list[0] == array[idx]:
                bomb_list.append(array[idx])
            else:
                # 다르고, 구슬 4개 이상이면 폭발
                if len(bomb_list) >= 4:
                    bomb_flag = 1
                    answer[bomb_list[0]] += len(bomb_list)
                    for _ in range(len(bomb_list)):
                        array.pop(idx+1)
                # 4개 이상이든, 이하이든 새로 bomb_list 갱신
                bomb_list = [array[idx]]

        # for문 끝났을 때 처리
        if len(bomb_list) >= 4:
            bomb_flag = 1
            answer[bomb_list[0]] += len(bomb_list)
            for _ in range(len(bomb_list)):
                array.pop(0)

    new_array = []
    cnt, old_num = 0, array[0] if array else 0
    for idx in range(len(array)):
        num = array[idx]
        # 이전 값이랑 현재 값이랑 같으면 cnt +1
        if num == old_num:
            cnt += 1
        # 다르면 new_array에 개수, 값 넣어주고 cnt, old_num 새로 갱신
        else:
            new_array.append(cnt)
            new_array.append(old_num)
            cnt, old_num = 1, num
    else:
        new_array.append(cnt)
        new_array.append(old_num)

    if len(new_array) > N * N - 1:
        new_array = new_array[:N*N-1]

    return array_to_matrix(new_array)



def matrix_to_array(matrix):
    # 왼, 하, 우, 상
    dr = [0, 1, 0, -1]
    dc = [-1, 0, 1, 0]

    array = []
    r, c = shark
    d, level, level_cnt = 0, 1, 0
    flag = 1

    # matrix[r][c]가 비어있을 때까지 반복
    while matrix[r][c]:

        for i in range(1, level+1):
            nr = r + dr[d] * i
            nc = c + dc[d] * i

            # 범위 바깥이면 X
            if not (0 <= nr < N and 0 <= nc < N):
                flag = 0
                continue

            # 비어있으면 끝내기
            if not matrix[nr][nc]:
                flag = 0
                break
            # 구슬 파괴면 result list에 추가
            elif matrix[nr][nc] != -2:
                array.append(matrix[nr][nc])

        # 마지막 nr, nc로 갱신
        if flag:
            r, c = nr, nc
        else:
            break

        # level cnt 증가, 방향 변경
        level_cnt += 1
        d = (d+1) % 4

        # 2번 count 했으면 레벨 올려주고 리셋
        if level_cnt == 2:
            level_cnt = 0
            level += 1

    return array

def array_to_matrix(array):
    dr = [0, 1, 0, -1]
    dc = [-1, 0, 1, 0]

    matrix = [[0]*N for _ in range(N)]
    r, c = shark
    matrix[r][c] = -1

    d, level, level_cnt = 0, 1, 0
    flag = 1

    array = array[:]
    while array:

        for i in range(1, level + 1):
            if array:
                marble = array.pop(0)
            else:
                flag = 0
                break

            nr = r + dr[d] * i
            nc = c + dc[d] * i

            # 범위 내이면 matrix 에 추가
            if 0 <= nr < N and 0 <= nc < N:
                matrix[nr][nc] = marble

        # 마지막 nr, nc로 갱신
        if flag:
            r, c = nr, nc
        else:
            break

        # level cnt 증가, 방향 변경
        level_cnt += 1
        d = (d + 1) % 4

        # 2번 count 했으면 레벨 올려주고 리셋
        if level_cnt == 2:
            level_cnt = 0
            level += 1

    return matrix


N, M = map(int ,input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
shark = (N//2, N//2)
matrix[N//2][N//2] = -1
answer = [0, 0, 0, 0]

for _ in range(M):
    d, s = map(int, input().split())
    matrix = marble_destory(d-1, s, matrix)

print(answer[1] + answer[2]*2 + answer[3]*3)
