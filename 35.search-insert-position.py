#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        if target <= nums[0]:
            return 0
        if target == nums[-1]:
            return len(nums) - 1
        if target > nums[-1]:
            return len(nums)
        left = 0
        right = len(nums) - 1
        result = -1
        while left <= right:
            middle = int((left + right)/2)
            value = nums[middle]
            if value == target:
                result = middle
                return result
            elif value < target:
                left = middle + 1
                result = middle + 1
            else:
                right = middle - 1
                result = middle
        return result
# @lc code=end

