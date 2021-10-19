import sys
sys.stdin = open('input.txt')
q = lambda : map(int, sys.stdin.readline().split())
sys.setrecursionlimit(10**9)

# 6060ms

# DP(i, true) = min(DP(i 의 자식, true), DP(i 의 자식, false))들의 총합 + 1
# i가 얼리어답터이면 자식은 얼리어답터여도 되고, 아니여도 되고

# DP(i, false) = DP(i 의 자식, true) 들의 총합
# i가 얼리어답터가 아니면, 자식은 반드시 얼리어답터

n = int(input())
graph  = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(n - 1):
  u, v = q()
  graph[u].append(v)
  graph[v].append(u)

# [정점 번호][얼리 어답터 체크]
dp = [[0, 0] for _ in range(n + 1)]
# 해당 노드가 얼리어답터가 아닐때, 맞을때 서브트리(자신 포함) 얼리어답터 최소수


def solve_dp(num):
  visited[num] = True
  dp[num][0] = 0 # 자식은 모르겠고 일단 내가 얼리어답터 아니니 0
  dp[num][1] = 1 # 자식은 모르겠고 일단 내가 얼리어답터니까 1

  for i in graph[num]: # 연결된 노드 중에서
    if not visited[i]: # 방문하지 않은 -> 결국 자식 노드가 됨
      solve_dp(i)
      dp[num][0] += dp[i][1] # 내가 얼리어답터 아니면, 자식은 반드시 얼리어답터
      dp[num][1] += min(dp[i][0], dp[i][1]) # 내가 얼리어답터면, 자식은 얼리어답터여도 되고 아니여도 됨

solve_dp(1)
print(min(dp[1][0], dp[1][1]))


