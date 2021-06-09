# 세그먼트 트리
# 배열의 구간합을 이진트리형태로 저장한 자료구조
# 트리를 탐색하므로 시간복잡도는 O(logn)

# 1. 구간합 트리의 길이는 배열길이의 4배로 설정
# 2. 왼쪽 자식은 구간합 범위의 왼쪽 절반, 오른쪽 자식은 오른쪽 절반에 매핑된다.

class SegTree:
    # 구간합 트리를 만든다.
    def init(self, start, end, node):
        if start == end:
            self.tree[node] = self.A[start]
        else:
            mid = (start + end) // 2
            self.tree[node] = self.init(start, mid, node * 2) + self.init(mid+1, end, node * 2 + 1)
        return self.tree[node]

    def __init__(self, A):
        self.A = A
        # 배열의 길이에 대해 2의 제곱 형태의 길이를 가지기 때문에 4를 곱하면 모든 범위를 커버할 수 있다.
        self.tree = [0] * len(A) * 4
        # segtree의 노드는 1부터 시작한다.
        self.init(0, len(A)-1, 1)

    # start, end : 시작 인덱스, 끝 인덱스
    # left, right : 구간합을 구하고자 하는 범위
    def sum(self, start, end, left, right, node):
        # 아예 범위 밖에 있는 경우 start end left right | left right start end
        if left > end or right < start:
            return 0
        # 범위 안에 있는 경우 left start end right
        if left <= start and right >= end:
            return self.tree[node]
        # 걸친 경우
        mid = (start+end) // 2
        return self.sum(start, mid, left, right, node*2) + self.sum(mid+1, end, left, right, node*2+1)

    # start, end : 배열의 시작인덱스, 끝 인덱스
    # target, value : 수정할 인덱스, 수정할 값(원래값에 더해준다.)
    def update(self, start, end, node, target, value):
        # 범위 밖에 있는 경우
        if target < start or target > end:
            return
        # 범위 안에 있으면
        self.tree[node] += value

        mid = (start + end) // 2
        self.update(start, mid, target, value, node * 2)
        self.update(mid+1, end, target, value, node * 2 + 1)

arr = [1, 9, 3, 8, 4, 5, 5, 9, 10, 3, 4, 5]
seg = SegTree(arr)
N = len(arr)
# 인덱스 0 ~ 11 구간합
print(seg.sum(0, N-1, 0, N-1, 1))
# 인덱스 3 ~ 8 구간합
print(seg.sum(0, N-1, 3, 8, 1))
# 인덱스 5의 원소를 -5 만큼 수정
seg.update(0, N-1, 1, 5, -5)
print(seg.sum(0, N-1, 0, N-1, 1))