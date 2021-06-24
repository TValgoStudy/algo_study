N = int(input())

quad_tree = [input() for _ in range(N)]


def compress_quad(half_n, matrix, start_row=0, start_col=0):
    cmp_value = matrix[start_row][start_col]
    flag = False
    for row in range(start_row, start_row+half_n*2):
        for col in range(start_col, start_col + half_n*2):
            if cmp_value != matrix[row][col]:
                flag = True
                break
        if flag:
            break
    if not flag:
        return cmp_value
    # 4 분할
    dr = [start_row, start_row, start_row + half_n, start_row + half_n]
    dc = [start_col, start_col + half_n, start_col, start_col + half_n]
    ans = '('
    for d in range(4):
        flag = True
        cmp_value = matrix[dr[d]][dc[d]]
        for row in range(dr[d], half_n + dr[d]):
            for col in range(dc[d], half_n + dc[d]):
                if cmp_value != matrix[row][col]:
                    flag = False
                    break
            if flag == False:
                break
        if flag == False:
            ans += compress_quad(half_n // 2, matrix, start_row=dr[d], start_col=dc[d])
        else:
            ans += cmp_value
    ans += ')'
    return ans


answer = compress_quad(N//2, quad_tree)
print(answer)