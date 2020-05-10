#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = int((right + left) / 2)
            if nums[middle] == target:
                return middle
            if nums[left] <= nums[middle]:
                if (nums[left] <= target) and (target <= nums[middle]):
                    right = middle - 1
                else:
                    left = middle + 1
            else:
                if (nums[middle] <= target) and (target <= nums[right]):
                    left = middle + 1
                else:
                    right = middle - 1
        return -1
# @lc code=end

