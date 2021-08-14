import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def solution(number, n, k):
    # 1. 자리수만큼의 구간내에서 최대값을 찾는다.
    M = n - k
    max_idx = number[:k+1].index(max(number[:k+1]))

    # 2. 최대값보다 전에 있는 값은 제거하고, 내가 제거한 숫자의 개수에 더한다.
    remove_count = max_idx
    number = number[max_idx:]

    # 3.
    fix = 1
    while fix < M:
        # 맨앞을 제외한 값중 최대값을 구함, 맨앞은 고정되었으니까!
        # fix는 내가 고정한 갯수, 앞에서 확정된 숫자 다음부터 최대값을 구해야하기 때문
        max_idx = fix
        # 확정값 다음부터, 내가 뺄수 있는개수+1까지 중에서 최대값을 찾음
        # 그 밖에서 최대값 구해봤자 제거할수 있는 개수를 넘어가서 그걸 붙여 쓸수 없음
        for i in range(fix, fix + k-remove_count + 1):
            if int(number[i]) == 9:
                max_idx = i
                break
            if int(number[i]) > int(number[max_idx]):
                max_idx = i
        # 최대인덱스를 구한 후, 그 사이에 있는건 빼버리자
        # 제거한 개수도 늘려주고, 확정된 값도 하나 늘었으니, 늘려주자
        number = number[:fix] + number[max_idx:]
        remove_count += max_idx - fix
        fix += 1

    return number[:M]


n, k = map(int, input().split())
number = input()

print(solution(number, n, k))