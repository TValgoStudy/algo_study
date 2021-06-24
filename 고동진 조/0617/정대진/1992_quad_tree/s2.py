N = int(input())

quad_tree = [input() for _ in range(N)]


def compress_quad(n, matrix, start_row=0, start_col=0):
    cmp_val = matrix[start_row][start_col]
    is_compress = True
    ans = '('
    for row in range(n):
        for col in range(n):
            if cmp_val != matrix[row][col]:
                is_compress = False
                break
        if not is_compress:
            break
    if not is_compress:
        half_n = n//2
        dr = [0, 0, half_n, half_n]
        dc = [0, half_n, 0, half_n]
        for d in range(4):
            ans += compress_quad(half_n, matrix, start_row=start_row+dr[d], start_col=start_col+dc[d])
    else:
        ans += cmp_val + ')'
    return ans


answer = compress_quad(N, quad_tree)
print(answer)