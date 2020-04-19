#
# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def calculate(root: TreeNode) -> TreeNode:
            if not root:
                return None
            left = root.left
            right = root.right
            root.left = None
            root.right = None
            result = root
            if left:
                result.right = left
                result = calculate(left)
            if right:
                result.right = right
                result = calculate(right)
            return result
        calculate(root)
        
# @lc code=end

