import sys
sys.stdin = open('input.txt')

# 문제 잘 이해하기
N = int(input())

cnt = 0
# 양의 정수 범위
for X in range(1, N+1):
    # 100보다 작으면 부조건 등차수열
    if X < 100:
        cnt += 1
    else:
        # 숫자 분리
        nums = list(map(int,str(X)))
        print(nums)
        cha = nums[0] - nums[1]
        # 등차수열 확인
        for i in range(1, len(nums)-1):
            if nums[i] - nums[i+1] != cha:
                break
        # else는 숫자제한 없는경우
        # 지금 문제에서는 없어도 된다
        else:
            cnt += 1
print(cnt)

