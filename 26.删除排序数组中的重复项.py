#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not len(nums):
            return
        i = 1
        while i < len(nums):
            element = nums[i]
            reference = nums[i - 1]
            if element == reference:
                del nums[i]
            else:
                i += 1
        return len(nums)


                
# @lc code=end

