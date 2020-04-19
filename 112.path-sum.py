#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
                return 0
        if (not root.left) & (not root.right):
            return sum == root.val
        target = sum - root.val
        left = self.hasPathSum(root.left, target)
        right = self.hasPathSum(root.right, target)
        return left | right
# @lc code=end

