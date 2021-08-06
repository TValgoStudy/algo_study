from sys import stdin
stdin = open("input5.txt", "r")

input = stdin.readline
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
d2 = [(-1, -1), (1, 1), (-1, 1), (1, -1), (-1, 0), (1, 0), (0, -1), (0, 1)]


def solve():
    N, M = map(int, input().split())
    board = []
    virus = []
    safeArea = []

    # 바이러스(2) 이면 바이러스에, 0이면 saftArea에 추가
    for i in range(N):
        board.append(list(map(int, input().split())))
        for j in range(len(board[i])):
            if board[i][j] == 2:
                virus.append((i, j))
            elif board[i][j] == 0:
                safeArea.append((i, j))
    
    # 주변에 벽에 있는지 탐색
    def nearWall(_x, _y, _board):
        l, r, u, d = False, False, False, False
        # 입력된 _x, _y에 대해 8방향 탐색
        for dx, dy in d2:
            x, y = _x + dx, _y + dy
            # up True
            if x < 0 or (x < _x and 0 <= y < M and _board[x][y] == 1):
                u = True
            # down True
            elif x >= N or (x > _x and 0 <= y < M and _board[x][y] == 1):
                d = True
            # left True
            if y < 0 or (y < _y and 0 <= x < N and _board[x][y] == 1):
                l = True
            # right True
            elif y >= M or (y > _y and 0 <= x < N and _board[x][y] == 1):
                r = True
            # 만약 4면이 다 True면 True반환
            if (l and r) or (u and d):
                return True
        # 그게아니면 False반환
        return False

    
    def countSafeCell(a, b, c):
        # board 카피 & 3곳 벽세우기
        _board = [[*board[i]] for i in range(len(board))]
        _board[a[0]][a[1]] = 1
        _board[b[0]][b[1]] = 1
        _board[c[0]][c[1]] = 1

        countSafeArea = len(safeArea) - 3
        if (nearWall(*a, _board) and nearWall(*b, _board) and nearWall(*c, _board)):
            
            # 바이러스 확산
            q = [*virus]
            idx = 0
            while idx != len(q):
                _x, _y = q[idx]
                idx += 1
                for dx, dy in d:
                    x, y = _x + dx, _y + dy
                    if 0 <= x < N and 0 <= y < M and _board[x][y] == 0:
                        q.append((x, y))
                        _board[x][y] = 2
                        countSafeArea -= 1
            return countSafeArea

        return 0

    # 벽을 세웠을 때 안전 영역의 최댓값 반환
    def buildWall():
        _ans = 0
        # 안전한 곳 저장해둔 리스트에서 3개 뽑기
        for i in range(len(safeArea)):
            for j in range(i + 1, len(safeArea)):
                for k in range(j + 1, len(safeArea)):
                    _ans = max(_ans, countSafeCell(safeArea[i], safeArea[j], safeArea[k]))
        return _ans

    return buildWall()


print(solve())