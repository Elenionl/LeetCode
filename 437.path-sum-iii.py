#
# @lc app=leetcode id=437 lang=python3
#
# [437] Path Sum III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        count = 0
        def calculate(root, sum, previous):
            nonlocal count
            if not root:
                return
            result = []
            for item in previous:
                newItem = item + root.val
                result.append(newItem)
                if newItem == sum:
                    count += 1
            if root.val == sum:
                count += 1
            result.append(root.val)
            calculate(root.left, sum, result)
            calculate(root.right, sum, result)
        calculate(root, sum, [])
        return count
# @lc code=end

