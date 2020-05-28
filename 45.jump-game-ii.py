#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        max_position = 0
        end = 0
        step = 0
        for i in range(n - 1):
            if max_position >= i:
                max_position = max(max_position, i + nums[i])
                if i == end:
                    end = max_position
                    step += 1
        return step

        
# @lc code=end

