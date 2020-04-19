#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        def compare(left: TreeNode, right: TreeNode) -> bool:
            if (not left or not right):
                return not left and not right
            elif (left.val != right.val):
                return False
            else:
                return compare(left.left, right.right) and compare(left.right, right.left)
        return compare(root.left, root.right)
        
# @lc code=end

