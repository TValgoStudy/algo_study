def solution(r: int, c: int, edge: int):
    if edge == 1:
        if image[r][c] == '1':
            return '1'
        else:
            return '0'
    else:
        next_edge = edge // 2
        total = 0
        for row in range(r, r + edge):
            for col in range(c, c + edge):
                total += int(image[row][col])

        if total == edge ** 2:
            return '1'
        elif total == 0:
            return '0'
        else:
            left_up = solution(r, c, next_edge)
            right_up = solution(r, c + next_edge, next_edge)
            left_down = solution(r + next_edge, c, next_edge)
            right_down = solution(r + next_edge, c + next_edge, next_edge)
            return '(' + left_up + right_up + left_down + right_down + ')'


# 왼쪽 위, 오른쪽 위, 왼쪽 아래, 오른쪽 아래.
N = int(input())
image = [list(input()) for _ in range(N)]
print(solution(0, 0, N))
