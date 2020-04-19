#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if (p == None) and (q == None):
            return True
        if (p == None) | (q == None):
            return False
        if p.val != q.val:
            return False
        leftResult = self.isSameTree(p.left, q.left)
        if not leftResult:
            return False
        rightResult = self.isSameTree(p.right, q.right)
        if not rightResult:
            return False
        return True
# @lc code=end

