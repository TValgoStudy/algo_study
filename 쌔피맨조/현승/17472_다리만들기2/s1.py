import sys
sys.stdin = open("input.txt", "r")

from pprint import pprint

from collections import deque

def bfs(i, j, num):
    q = deque([(i, j)])
    visited[i][j] = 1
    arr[i][j] = num
    while q:
        x, y = q.popleft()
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = 1
                arr[nx][ny] = num
                q.append((nx, ny))

def dfs(is_col, idx, total):
    print(is_col, idx, total, check)
    global ans, k, num

    if not is_col and idx == N:
        is_col = True
        idx = 0

    standard = check[1]
    for i in range(2, num + 1):
        if not check[i] or check[i] != standard:
            break
    else:
        is_col = True
        idx = M

    if is_col and idx == M:
        standard = check[1]
        for i in range(2, num + 1):
            if not check[i] or check[i] != standard:
                return
        else:
            print('다왔다.', total)
            if total < ans:
                ans = total
            return

    if total > ans:
        return


    region1, region2 = 0, 0
    flag = 0
    road_len = 0
    if is_col:
        flag = 0
        road_len = 0
        for x in range(N):
            # 섬일 때
            if arr[x][idx]:
                # 처음 섬을 만남
                if flag == 0:
                    flag = 1
                    region1 = arr[x][idx]
                # 두번째 섬을 만남
                elif flag == 2:
                    if road_len > 1:
                        region2 = arr[x][idx]
                        flag = 3
                        break
                    else:
                        flag = 1
                        region1 = arr[x][idx]
                        road_len = 0
            # 땅일 때
            else:
                # 첫 번째 섬이었다가 땅을만남 -> flag = 2
                if flag == 1:
                    flag = 2
                # 첫 번재 섬을 지남 => 길갯수세기
                if flag == 2:
                    road_len += 1
    else:
        for y in range(M):
            # 섬일 때
            if arr[idx][y]:
                # 처음 섬을 만남
                if flag == 0:
                    flag = 1
                    region1 = arr[idx][y]
                # 두번째 섬을 만남
                elif flag == 2:
                    if road_len > 1:
                        region2 = arr[idx][y]
                        flag = 3
                        break
                    else:
                        flag = 1
                        region1 = arr[idx][y]
                        road_len = 0
            # 땅일 때
            else:
                # 첫 번째 섬이었다가 땅을만남 -> flag = 2
                if flag == 1:
                    flag = 2
                # 첫 번재 섬을 지남 => 길갯수세기
                if flag == 2:
                    road_len += 1
    # 길이 연결된 경우 다음 레벨로 가러 출발
    if flag == 3:
        if not (check[region1] and check[region2]):
            if not check[region1] and check[region2]:
                check[region1] = check[region2]
                dfs(is_col, idx + 1, total + road_len)
                check[region1] = 0
            elif check[region1] and not check[region2]:
                check[region2] = check[region1]
                dfs(is_col, idx + 1, total + road_len)
                check[region2] = 0
            else:
                k += 1
                check[region1], check[region2] = k, k
                dfs(is_col, idx + 1, total + road_len)
                k -= 1
                check[region1], check[region2] = 0, 0
        # 둘다 방문기록은 있는데 분리되어 있는 지역인 경우 한 색깔로 묶어주기
        elif check[region1] != check[region2]:
            tmp = check[region2]
            region_list = []
            for i in range(1, num+1):
                if check[i] == tmp:
                    # print(i, end=' ')
                    region_list.append(i)
                    check[i] = check[region1]
            # print('다바꼈나??', check, check[region1])
            dfs(is_col, idx+1, total + road_len)
            for i in region_list:
                check[i] = tmp

    # 길 포함하지 않고 다음 인덱스 보기
    dfs(is_col, idx + 1, total)


N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

# 섬의 영역 표시하기 bfs
num = 0
visited = [[0 for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        if not visited[i][j] and arr[i][j]:
            num += 1
            bfs(i, j, num)
pprint(arr)
# 각 섬 번호에 대해 연결되어 있는 지 체크
k = 0
check = [0 for _ in range(num+1)]

# 행인지 열인지랑 인덱스 / 행이면 방향 (0, 1)이고 열이면 방향 (1, 0)
# 행이면 0이고 열이면 1
ans = 9876543210
dfs(False, 0, 0)
print(ans)

