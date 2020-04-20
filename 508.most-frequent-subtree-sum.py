#
# @lc app=leetcode id=508 lang=python3
#
# [508] Most Frequent Subtree Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        result = {}
        def calculate(root):
            if not root:
                return 0
            value = calculate(root.left) + calculate(root.right) + root.val
            if not value in result:
                result[value] = 1
            else:
                result[value] = result[value] + 1
            return value
        calculate(root)
        maxResult = max(result.values())
        resultArray = []
        for k in result:
            v = result[k]
            if v == maxResult:
                resultArray.append(k)
        return resultArray

# @lc code=end

