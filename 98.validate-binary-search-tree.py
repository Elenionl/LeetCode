#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        left = float('-inf')
        def validate(root: TreeNode) -> bool:
            nonlocal left
            if not root:
                return True
            if not validate(root.left):
                return False
            if root.val <= left:
                return False
            else:
                left = root.val
            if not validate(root.right):
                return False
            return True
        return validate(root)
        
# @lc code=end

