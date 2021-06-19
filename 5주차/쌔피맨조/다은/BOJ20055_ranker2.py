from collections import deque

N,K=map(int,input().split())
A=deque(map(int,input().split()))
level=r=0
robot=deque([0]*N)

while A.count(0) < K:
    A.rotate(1)
    robot.rotate(1)
    robot[-1] = 0

    for i in range(N-1, 0, -1):
        if robot[i-1] == 1 and robot[i] == 0 and A[i] > 0:
            A[i] -= 1
            robot[i-1] = 0
            robot[i] = 1

    robot[-1]=0

    if robot[0] == 0 and A[0] > 0:
        robot[0] = 1
        A[0] -= 1

    level+=1

print(level)