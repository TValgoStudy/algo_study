
import sys
sys.stdin = open('input.txt', 'r')
# 인풋 받는 함수
def get_input():
    N = [int(n) for n in input().split(' ')[:2]]
    _map = list()
    for i in range(N[0]):
        _map.append([int(x) for x in input().split(' ')[:N[1]]])
    return N[0], N[1], _map

# 바이러스 퍼뜨리고 세는 함수 (기본 맵 받아옴)
def spreadAndCount(_map):
    # 안전한 곳 세는 함수
    def count_safe(_map):
        # 전체 구한다음
        count = (len(_map)) * (len(_map[0]))
        # 순회하면서
        for row in _map:
            # 1이랑 2 만큼 뺌
            count = count - row.count(1) - row.count(2)
        return count
    # 맵 복사
    result = [x[:] for x in _map]
    # 가로세로 계산
    N = len(_map)
    M = len(_map[0])

    # 빈 리스트(큐)
    queue = list()
    # 순회하면서 바이러스가 있으면 좌표값을 큐에 튜플 형태로 넣는다
    for i in range(1, N - 1):
        for j in range(1, M - 1):
            if result[i][j] == 2:
                queue.append((i,j))

    while(True):
        # 새로운 큐
        new_queue = []
        # 튜플(인덱스, 값)
        for i, x in enumerate(queue):
            # 아까 저장한 파이러스 좌표
            i, j = x[0], x[1]
            # 상하좌우가 벽아니고 바이러스 없으면 바이러스 퍼트림
            if result[i-1][j] not in (1, 2):
                result[i - 1][j] = 2
                # 새 큐에다가 이동한 퍼진 넣음
                new_queue.append((i-1,j))
            if result[i+1][j] not in (1, 2):
                result[i + 1][j] = 2
                new_queue.append((i+1,j))
            if result[i][j-1] not in (1, 2):
                result[i][j-1] = 2
                new_queue.append((i,j-1))
            if result[i][j+1] not in (1, 2):
                result[i][j+1] = 2
                new_queue.append((i,j+1))
        queue = new_queue
        # 큐 비면 안전지대 세기
        if not queue:
            return count_safe(result)

# 벽 고르기
def set_wall(_map, num=1):
    def check_8neighbor(inp_map, n, m):  # 상하좌우대각 8칸 확인
        score = 0
        #
        for a in range(n - 1, n + 2):
            for b in range(m - 1, m + 2):
                if inp_map[a][b] == 1:
                    score += 1
        if score >= 1:
            return True
        else:
            return False

    N = len(_map)
    M = len(_map[0])
    crnt_map = [x[:] for x in _map]  # deep copy

    maximum = 0
    count = 0
    # set candidate
    candidate = list()
    for n in range(1, N-1):
        for m in range(1, M-1):
            if crnt_map[n][m] == 0 and check_8neighbor(crnt_map, n, m):
                candidate.append((n, m))

    for w in candidate:
        crnt_map[w[0]][w[1]] = 1  # set wall
        if num == 1:
            count = set_wall(crnt_map, num + 1)
            crnt_map[w[0]][w[1]] = 3  # 지나갔던 곳
        if num == 2:
            count = set_wall(crnt_map, num + 1)
            crnt_map[w[0]][w[1]] = 4  # 지나갔던 곳
        if num == 3:
            count = spreadAndCount(crnt_map)  # spread the plague And measure the area of safe zone
            crnt_map[w[0]][w[1]] = 5  # 지나갔던 곳
            if maximum < count:
                maximum = count
            continue

        if maximum < count:
            maximum = count

    return maximum


def isolate(_map):
    M = len(_map[0])
    # padding
    inp_map = [[1 for _ in range(M)]] + _map
    for i, m in enumerate(inp_map):
        inp_map[i] = [1] + m + [1];
    inp_map.append([1 for _ in range(M+2)])

    res = set_wall(inp_map)  # dynamic programming, DFS

    return res


if __name__ == "__main__":
    N, M, _map = get_input()
    result = isolate(_map)
    print(result)
