#
# @lc app=leetcode id=222 lang=python3
#
# [222] Count Complete Tree Nodes
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        leftDepth = self.depth(root.left)
        rightDepth = self.depth(root.right)
        if leftDepth == rightDepth:
            return pow(2, leftDepth) + self.countNodes(root.right)
        else:
            return self.countNodes(root.left) + pow(2, rightDepth)
    def depth(self, root) -> int:
            if not root:
                return 0
            return 1 + self.depth(root.left)
        
# @lc code=end

