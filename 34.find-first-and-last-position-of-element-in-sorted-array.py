#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = -1
        left = 0
        right = len(nums) - 1
        middle = -1
        while right >= left:
            middle = int((left + right) / 2)
            value = nums[middle]
            if value == target:
                result = middle
                break
            elif value < target:
                left = middle + 1
            else:
                right = middle - 1
        array = [result, result]
        while array[0] > 0:
            newValue = array[0] - 1
            if nums[newValue] == target:
                array[0] = newValue
            else:
                break
        while array[1] < (len(nums) - 1):
            newValue = array[1] + 1
            if nums[newValue] == target:
                array[1] = newValue
            else:
                break
        return array

        
# @lc code=end

