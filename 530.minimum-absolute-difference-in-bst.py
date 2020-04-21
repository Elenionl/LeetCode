#
# @lc app=leetcode id=530 lang=python3
#
# [530] Minimum Absolute Difference in BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        cache = float('inf')
        previous = None
        def calculate(root):
            if not root:
                return
            calculate(root.left)
            nonlocal cache
            nonlocal previous
            if previous:
                distance = root.val - previous.val
                if distance < cache:
                    cache = distance
            previous = root
            calculate(root.right)
        calculate(root)
        return cache


# @lc code=end

