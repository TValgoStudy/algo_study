import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**9)

# 584ms

N = int(input())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N+1)
arr = [0] + list(map(int, input().split()))

# n번 노드가 우수마을인 경우 / 아닌 경우 서브트리의 최대인원
dp = [[0] * (N+1) for _ in range(2)]

for _ in range(N-1):
    v, w = map(int, input().split())
    graph[v].append(w)
    graph[w].append(v)


def goodVillage(v):
    visited[v] = 1
    # dp[0][v] = 0  # 우수마을 아닌 경우 -> 주석 처리하면 584ms
    dp[1][v] = arr[v] # 우수마을인 경우

    for w in graph[v]:  # 연결된 노드 중에서
        if not visited[w]:  # 방문하지 않은 -> 결국 자식 노드가 됨
            goodVillage(w)
            dp[0][v] += max(dp[1][w], dp[0][w])  # 내가 우수 마을이 아니면, 자식은 우수마을이여도 되고 아니여도 되고
            dp[1][v] += dp[0][w]  # 내가 우수마을이면, 자식은 우수마을이 아님


goodVillage(1)
print(max(dp[0][1], dp[1][1]))


