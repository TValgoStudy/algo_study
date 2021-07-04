import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline().rstrip())
max_ = [0] * 3
min_ = [0] * 3

for i in range(N):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())

    max_[0], max_[1], max_[2] = max_[0] + a if max_[0] > max_[1] else max_[1] + a, max(max_) + b, max_[1] + c if max_[
                                                                                                                     1] > \
                                                                                                                 max_[
                                                                                                                     2] else \
    max_[2] + c
    min_[0], min_[1], min_[2] = min_[0] + a if min_[0] < min_[1] else min_[1] + a, min(min_) + b, min_[1] + c if min_[
                                                                                                                     1] < \
                                                                                                                 min_[
                                                                                                                     2] else \
    min_[2] + c

print(max(max_), min(min_))