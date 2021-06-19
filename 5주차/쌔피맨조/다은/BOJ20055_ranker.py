from collections import deque
import sys

input = sys.stdin.readline
n,k = map(int,input().split())
A = deque(map(int,input().split()))
ans =1

#robot이 들어온 순서대로 현재 자신의 위치를 담고있는다
robot =deque([0]*(n*2))

while(True):
    #1
    A.rotate(1)
    robot.rotate(1)
    robot[n-1]=0 #내려가는 위치에 로봇 삭제

    #2
    for i in range(n-2,-1,-1):
        if(robot[i]!=0 and robot[i+1]==0 and A[i+1]>=1):
            A[i+1]-=1
            robot[i+1]=robot[i]
            robot[i]=0
    robot[n-1]=0

    #3
    if(robot[0]==0 and A[0]>0):
        A[0]-=1
        robot[0]=1

    #4
    cnt=0
    for i in range(len(A)):
        if(A[i]==0):
            cnt+=1

    if(cnt>=k):
        print(ans)
        break

    ans+=1