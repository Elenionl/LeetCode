#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        result = []
        def calculate(root, depth):
            nonlocal result
            if not root:
                return
            if depth >= len(result):
                result.append(root.val)
            calculate(root.right, depth + 1)
            calculate(root.left, depth + 1)
        calculate(root, 0)
        return result
        
# @lc code=end

