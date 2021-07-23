import sys
sys.stdin = open('input.txt')


def findChild():
    temp = [[] for _ in range(N)]
    root = 0

    for n in range(N):
        if P[n] != -1:
            temp[P[n]].append(n)
        else:
            root = n # root가 0인줄 알았으나 문제에선 그런말 한적 없음

    return temp, root


def DFS(n):
    global answer

    if n == removeNode: # 제거할 노드일 때
        if len(child[P[n]]) == 1: # 형제노드가 없으면 부모가 리프 노드가 되므로
            answer += 1
        return

    if not child[n]:
        answer += 1
        return

    for m in child[n]:
        DFS(m)


N = int(input())
P = list(map(int, input().split()))
removeNode = int(input())
child, root = findChild()
answer = 0

DFS(root)
print(answer)