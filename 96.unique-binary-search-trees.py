#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#

# @lc code=start
class Solution:
    def numTrees(self, n: int) -> int:
        offset = {0: 1}
        def generateTree(fromValue: int, toValue: int) -> int:
            if (toValue - fromValue) in offset:
                return offset[toValue - fromValue]
            result = 0
            for i in range(fromValue, toValue):
                left = generateTree(fromValue, i)
                right = generateTree(i + 1, toValue)
                result += left * right
            offset[toValue - fromValue] = result
            return result
        return generateTree(1, n + 1)
# @lc code=end

