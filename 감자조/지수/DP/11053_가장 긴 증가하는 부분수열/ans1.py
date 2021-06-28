import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# 시간 복잡도 O(nlogn)
# https://namu.wiki/w/%EC%B5%9C%EC%9E%A5%20%EC%A6%9D%EA%B0%80%20%EB%B6%80%EB%B6%84%20%EC%88%98%EC%97%B4#s-3.1

def lower(l, r, x):
    while l <= r:
        m = (l + r) // 2
        if v[m] >= x: # 찾는 값이 더 작으면 좌측으로 이동
            r = m - 1
        else: # 더 크면 우측으로 이동
            l = m + 1
    return l # 교차되었을 때의 l이 x의 자리

n=int(input())
arr=list(map(int,input().split()))
v=[arr[0]]

for i in range(1,n):
    if v[-1] < arr[i]: # 마지막 원소보다 크면, 맨뒤에 붙여서 LIS 추가
        v.append(arr[i])
    else: # 아닌 경우 자리를 찾아서 들어가기(lower bound 찾기)
        v[lower(0, len(v)-1, arr[i])] = arr[i]

print(len(v))

# 실제 v에 담기는 요소들이 LIS의 원소는 아니다.
# 단지 최장 길이를 확인 하기 위한 요소이다.