#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pre = 0
        max_answer = nums[0]
        for item in nums:
            pre = max(pre + item, item)
            max_answer = max(max_answer, pre)
        return max_answer

# @lc code=end

