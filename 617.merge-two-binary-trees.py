#
# @lc app=leetcode id=617 lang=python3
#
# [617] Merge Two Binary Trees
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if (not t1) and (not t2):
            return
        result = None
        if t1 and t2:
            result = TreeNode(t1.val + t2.val)
        elif t1:
            result = t1
        elif t2:
            result = t2
        left1 = None
        if t1:
            left1 = t1.left
        right1 = None
        if t1:
            right1 = t1.right
        left2 = None
        if t2:
            left2 = t2.left
        right2 = None
        if t2:
            right2 = t2.right
        result.left = self.mergeTrees(left1, left2)
        result.right = self.mergeTrees(right1, right2)
        return result
# @lc code=end

