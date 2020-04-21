#
# @lc app=leetcode id=572 lang=python3
#
# [572] Subtree of Another Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def isEqual(s, t) -> bool:
            if (not s) and (not t):
                return True
            if (not s) or (not t):
                return False
            if s.val != t.val:
                return False
            return isEqual(s.left, t.left) and isEqual(s.right, t.right)
        def calculate(s, t) -> bool:
            if not s:
                return False
            if (s.val == t.val) and isEqual(s, t):
                return True
            return calculate(s.left, t) or calculate(s.right, t)
        return calculate(s, t)
            
        
# @lc code=end

