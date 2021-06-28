import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(10000000)

# 4088 ms

n = int(input())
adj = [[] for i in range(n+11)]
for i in range(n-1):
    a,b = map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)

def dfs(u,p):
    mark = False # 내가 얼리어답터인지 아닌지
    num = 0 # 서브트리의 최소 얼리어답터 수
    for v in adj[u]:
        if v==p: continue # 인접노드가 부모인 경우 스킵
        tmp, m = dfs(v,u) # tmp: v를 root로 하는 서브트리의 최소 얼리어탑터 수 / m : v가 얼리어답터인지 아닌지
        num+=tmp
        if not m: mark=True # m 이 False 인경우 = 자식이 얼리어답터가 아님 = 내가 얼리어답터여야 함
    if mark: num+=1 # 내가 얼리어답터니까 +1
    return num, mark

print(dfs(1,0)[0])