#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def balanceAndDepth(root: TreeNode) -> int:
            if not root:
                return 0
            left = balanceAndDepth(root.left)
            right = balanceAndDepth(root.right)
            if (left == -1) or (right == -1):
                return -1
            if (left - right < 2) & (left - right > -2):
                return max(left, right) + 1
            else:
                return -1
        result = balanceAndDepth(root)
        return (result != -1)
        
# @lc code=end

