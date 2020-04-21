#
# @lc app=leetcode id=538 lang=python3
#
# [538] Convert BST to Greater Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        total = 0
        def calculate(root):
            if not root:
                return
            calculate(root.right)
            nonlocal total
            total += root.val
            root.val = total
            calculate(root.left)
        calculate(root)
        return root
            
# @lc code=end

