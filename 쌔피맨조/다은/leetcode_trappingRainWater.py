# https://leetcode.com/problems/trapping-rain-water/
# 파이썬 알고리즘 인터뷰 배열 - Q8 빗물 트래핑
# https://leetcode.com/problems/trapping-rain-water-ii/

# 풀이 1. 투 포인터를 최대로 이동
from typing import List

class Solution1:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        volume = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]

        while left < right:
            left_max, right_max = max(height[left], left_max), max(height[right], right_max)
            # 더 높은 쪽을 향해 투 포인터 이동
            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1
        return volume


#  풀이 2. 스택 쌓기
from typing import List

class Solution2:
    def trap(self, height: List[int]) -> int:
        stack = []
        volume = 0

        for i in range(len(height)):
            # 변곡점을 만나는 경우
            while stack and height[i] > height[stack[-1]]:
                # 스택에서 꺼낸다
                top = stack.pop()

                # 스택이 비었으면 중지
                if not len(stack):
                    break

                # 이전과의 차이만큼 물 높이 처리
                distance = i - stack[-1] - 1
                waters = min(height[i], height[stack[-1]]) - height[top]

                volume += distance * waters

            stack.append(i)
        return volume

height = [0,1,0,2,1,0,1,3,2,1,2,1]
test = Solution1()
print(test.trap(height))