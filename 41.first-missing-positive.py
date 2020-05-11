#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#

# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        length = len(nums)
        def swap(nums, left, right):
            value = nums[left]
            nums[left] = nums[right]
            nums[right] = value
        for index in range(length):
            while 1 <= nums[index] <= length and nums[index] != nums[nums[index] - 1]:
                swap(nums, index, nums[index] - 1)
        for i in range(length):
            if i + 1 != nums[i]:
                return i + 1

        return length + 1

# @lc code=end

