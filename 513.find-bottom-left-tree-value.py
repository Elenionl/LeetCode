#
# @lc app=leetcode id=513 lang=python3
#
# [513] Find Bottom Left Tree Value
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        node = None
        maxDepth = 0
        def claculate(root, depth):
            if not root:
                return
            nonlocal node
            nonlocal maxDepth
            claculate(root.left, depth + 1)
            if not root.left and not root.right:
                if depth > maxDepth:
                    maxDepth = depth
                    node = root
                return
            claculate(root.right, depth + 1)
        claculate(root, 1)
        if not node:
            return None
        return node.val
        
# @lc code=end

