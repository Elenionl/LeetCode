#
# @lc app=leetcode id=563 lang=python3
#
# [563] Binary Tree Tilt
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTilt(self, root: TreeNode) -> int:
        sum = 0
        def claculate(root) -> int:
            if not root:
                return 0
            left = claculate(root.left)
            right = claculate(root.right)
            nonlocal sum
            sum += abs(left - right)
            return left + right + root.val
        claculate(root)
        return sum
        
# @lc code=end

