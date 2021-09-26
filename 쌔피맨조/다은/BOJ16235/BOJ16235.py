import sys
from pandas import DataFrame
sys.stdin = open("input.txt", "r")

N, M, K = map(int, input().split())

food = [[5]*N for _ in range(N)]
winter_food = [list(map(int, input().split())) for _ in range(N)]

tree_map = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    r, c, age = map(int, input().split())
    tree_map[r-1][c-1].append(age)

dr = [-1, 1, 0, 0, -1, -1, 1, 1]
dc = [0, 0, -1, 1, -1, 1, -1, 1]

year = 0
while year != K:
    # 봄
    for r in range(N):
        for c in range(N):
            # tree_map의 list에 접근해서, 나이가 어린 나무부터 양분 먹도록 정렬시킴
            tree_map[r][c].sort()
            current_food = food[r][c]
            next_tree = []
            next_food = 0
            # for문으로 tree_map의 list 순회
            for i in range(len(tree_map[r][c])):
                # 양분을 줄 수 있으면 주고, 양분에서 뺀 후 next_tree에 성장시켜서 넣어두기
                if current_food >= tree_map[r][c][i]:
                    current_food -= tree_map[r][c][i]
                    next_tree.append(tree_map[r][c][i] + 1)
                # 양분을 줄 수 없으면 죽음 => 여름
                else:
                    next_food += tree_map[r][c][i] // 2
            tree_map[r][c] = next_tree
            food[r][c] = current_food + next_food

    # 가을
    for r in range(N):
        for c in range(N):
            # for 문으로 tree_map의 list 순회
            for i in range(len(tree_map[r][c])):
                # 나무의 나이가 5의 배수이면
                if not (tree_map[r][c][i] % 5):
                    # 8방향으로, 범위 내인 곳에 나이 1짜리 가 생긴다
                    for j in range(8):
                        nr = r + dr[j]
                        nc = c + dc[j]
                        if 0 <= nr < N and 0 <= nc < N:
                            tree_map[nr][nc].append(1)
    # 겨울
    for r in range(N):
        for c in range(N):
            food[r][c] += winter_food[r][c]

    year += 1

result = 0
for r in range(N):
    for c in range(N):
        result += len(tree_map[r][c])

print(result)
