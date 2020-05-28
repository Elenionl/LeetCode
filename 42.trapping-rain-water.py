#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        holding = 0
        left_to_right = []
        right_to_left = []
        max_height = 0
        for index in range(len(height)):
            value = height[index]
            max_height = max(max_height, value)
            left_to_right.append(max_height)
        
        
# @lc code=end

