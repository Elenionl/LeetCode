#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        bigest = 0
        def calculate(root) -> int:
            if not root:
                return 0
            left = calculate(root.left)
            right = calculate(root.right)
            length = left + right + 1
            nonlocal bigest
            if length > bigest:
                bigest = length
            return max(left, right) + 1
        calculate(root)
        return bigest - 1
# @lc code=end

