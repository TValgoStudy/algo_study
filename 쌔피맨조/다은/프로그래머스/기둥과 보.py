from pandas import DataFrame
# x   기둥   보   둘 다
# 0    -2    2    -4
#       0    1
def is_column(x, y):
    k = _map[x][y]
    if k == -2 or k == -4:
        return True
    return False

def is_grider(x, y):
    k = _map[x][y]
    if k == 2 or k == -4:
        return True
    return False

def can_column(x, y):
    # 바닥 위 or 또 다른 기둥 위 인가? == (x, y-1)에 기둥이 있는가?
    if y == 0 or is_column(x, y - 1):
        return True
    # 보의 한 쪽 끝 위 인가? == (x, y) or (x-1, y)에 보가 있는가?
    if is_grider(x, y) or is_grider(x - 1, y):
        return True
    return False

def can_girder(x, y):
    # 한 쪽이 기둥 위인가? == (x, y-1) or (x+1, y-1)에 기둥이 있는가?
    if is_column(x, y - 1) or is_column(x + 1, y - 1):
        return True
    # 양쪽 끝이 보인가? == (x-1, y) and (x+1, y)에 보가 있는가?
    if is_grider(x - 1, y) and is_grider(x + 1, y):
        return True
    return False


def can_delete():
    for a in range(N):
        for b in range(N):
            if _map[a][b] == -2:
                if not can_column(a, b): return False
            elif _map[a][b] == 2:
                if not can_girder(a, b): return False
            elif _map[a][b] == -4:
                if not can_column(a, b): return False
                if not can_girder(a, b): return False
    return True

# x   기둥   보   둘 다
# 0    -2    2    -4

# x,y  &  a=0(기둥->-2) or 1(보->2)  & b=0(삭제) or 1(추가)
def solution(n, build_frame):
    global N, _map
    N = n + 1

    _map = [[0] * N for _ in range(N)]
    for x, y, a, b in build_frame:
        w = 2 if a else -2
        if b:
            if w == -2:
                if can_column(x, y):
                    # 자신 추가
                    _map[x][y] = _map[x][y] * w if _map[x][y] else w
            else:
                if can_girder(x, y):
                    # 자신 추가
                    _map[x][y] = _map[x][y] * w if _map[x][y] else w
        else:
            # 일단 삭제 : 둘 다 있으면 자기만 삭제, 자기만 있으면 0
            _map[x][y] = _map[x][y] // w if _map[x][y] == -4 else 0
            # 삭제 불가면 다시 추가 : 아무것도 없으면 자신w 다른 것이 있으면 * w
            if not can_delete():
                _map[x][y] = w if _map[x][y] == 0 else _map[x][y] * w

    result = []
    for x in range(N):
        for y in range(N):
            if _map[x][y] == -2:
                result.append([x, y, 0])
            elif _map[x][y] == 2:
                result.append([x, y, 1])
            elif _map[x][y] == -4:
                result.append([x, y, 0])
                result.append([x, y, 1])
    return result

n = 5
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
print(solution(n, build_frame))