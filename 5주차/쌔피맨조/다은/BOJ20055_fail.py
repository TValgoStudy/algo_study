# 컨베이어 벨트 위의 로봇 20055

import sys
sys.stdin = open("input.txt", "r")

# 1번 칸이 있는 위치를 "올리는 위치", N번 칸이 있는 위치를 "내리는 위치"
# 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료
N, K = map(int, input().split())
belt = [9999] + list(map(int, input().split()))
robot = [0] * (2*N + 1)
robot_pos = []

result = 0
up, down = 1, N

while belt.count(0) < K:
    # 1단계
    up = 2 * N if up == 1 else up - 1
    down = 2 * N if down == 1 else down - 1
    if robot[down]:
        robot[down] = 0
        robot_pos.pop(0)

    # 2단계
    for i in range(len(robot_pos)):
        tmp = robot_pos[i]
        next_tmp = 1 if tmp == 2 * N else tmp + 1
        if tmp != down and belt[next_tmp] and not robot[next_tmp]:
            robot_pos[i] = next_tmp
            robot[next_tmp], robot[tmp] = 1, 0
            belt[next_tmp] -= 1
    if robot[down]:
        robot[down] = 0
        robot_pos.pop(0)

    # 3단계
    if belt[up] and not robot[up]:
        belt[up] -= 1
        robot[up] = 1
        robot_pos.append(up)

    # 4단계
    result += 1

print(result)
