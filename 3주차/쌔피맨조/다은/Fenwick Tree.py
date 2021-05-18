# 출처 https://www.youtube.com/watch?v=fg2iGP4e2mc

n = 17
arr = [0, 3, 2, 5, 7, 10, 3, 2, 7, 8, 2, 1, 9, 5, 10, 7, 4]
tree = [0] * n

# i번째 수 까지의 누적 합을 계산하는 함수
def prefix_sum(i):
    result = 0
    while i > 0:
        result += tree[i]
        i -= (i & -i)      # 마지막 1을 빼가면서 이동
    return result


# i번째 수를 dif만큼 더하는 함수
def update(i, dif):
    while i <= n:
        print("2진수로 {}, 10진수로 {}".format(bin(i)[2:], i))
        tree[i] += dif
        i += (i & -i)      # 마지막 1을 더하면서 이동


# start부터 end까지의 구간 합을 계산하는 함수
def interval_sum(start, end):
    return prefix_sum(end) - prefix_sum(start - 1)


# 트리 만들기
for i in range(1, n):
    update(i, arr[i])

print(tree)
print('---------------')
# 13번 인덱스를 업데이트하기
update(13, 2)

