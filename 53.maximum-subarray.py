#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pre = 0
        max_value = nums[0]
        for value in nums:
            pre = max(pre + value, value)
            max_value = max(max_value, pre)
        return max_value
                



            
# @lc code=end

