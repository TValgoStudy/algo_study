import heapq

def dijkstra(s):
    dist = [999999999] * (N + 1)
    dist[s] = 0
    q = []
    heapq.heappush(q, (0, s))
    while q:
        # 제일 작은 노드 선택
        current_dist, v = heapq.heappop(q)
        # 인접 정점들 중에서 dist[w]보다 경유하는게 더 짧으면 갱신
        for w in range(N + 1):
            if G[v][w] and dist[w] > dist[v] + G[v][w]:
                dist[w] = dist[v] + G[v][w]
                heapq.heappush(q, (dist[w], w))
    return dist


def solution(n, s, a, b, fares):
    global N, G
    N = n
    G = [[0] * (n + 1) for _ in range(n + 1)]
    for x, y, f in fares:
        G[x][y] = f
        G[y][x] = f
    s_dijkstra = dijkstra(s)
    a_dijkstra = dijkstra(a)
    b_dijkstra = dijkstra(b)

    fee = 99999999
    for k in range(1, N + 1):
        fee_tmp = s_dijkstra[k] + a_dijkstra[k] + b_dijkstra[k]
        if fee > fee_tmp:
            fee = fee_tmp
    return fee


n = 6
s = 4
a = 6
b = 2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
print(solution(n, s, a, b, fares))