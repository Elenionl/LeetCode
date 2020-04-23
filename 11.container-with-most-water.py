#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        left = 0
        right = len(height) - 1
        while right > left:
            leftValue = height[left]
            rightValue = height[right]
            result = max(result, min(leftValue, rightValue) * (right - left))
            if leftValue < rightValue:
                left += 1
            else:
                right -= 1
        return result
# @lc code=end

