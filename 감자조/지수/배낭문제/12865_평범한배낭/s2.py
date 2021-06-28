import sys
sys.stdin = open('input.txt')
q = lambda : map(int, sys.stdin.readline().split())

N, K = q()
item = [[0, 0]]
knapsack = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for _ in range(N):
    item.append(list(q()))


for i in range(1, N + 1): # 현재 넣으려는 물건 인덱스
    weight, value = item[i]
    for j in range(1, K + 1): # 현재 가방의 무게
        if j < weight: # 아이템 무게가 더 크면 넣을 수 없음 -> 선택지가 없음
            knapsack[i][j] = knapsack[i - 1][j]  # 현재 아이템을 안넣은 상태 = 이전물건까지 담긴 가방의 상태 가져오기
        else: # 현재 물건을 넣을 수 있음
            # value + knapsack[i - 1][j - weight]
                # value : 현재 물건 가치
                # knapsack[i - 1][j - weight] : 가방 용량이 j - weight 일때 이전 물건이 담겨진 상태
                # 즉, 현재 물건을 넣을꺼니까 이 물건 넣기 전 가방의 최상의 상태를 가져오는 것
            knapsack[i][j] = max(value + knapsack[i - 1][j - weight], knapsack[i - 1][j])

print(knapsack[N][K])