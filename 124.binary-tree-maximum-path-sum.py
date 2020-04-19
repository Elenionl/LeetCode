#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        total: int = float('-inf')
        def calculate(root) -> int:
            nonlocal total
            if not root:
                return float('-inf')
            left = calculate(root.left)
            right = calculate(root.right)
            if left > total:
                total = left
            if right > total:
                total = right
            if (left + right + root.val) > total:
                total = left + right + root.val
            convertable = max((left + root.val), (right + root.val))
            convertable = max(convertable, root.val)
            if convertable > total:
                total = convertable
            return convertable
        calculate(root)
        return total
        
        
# @lc code=end

