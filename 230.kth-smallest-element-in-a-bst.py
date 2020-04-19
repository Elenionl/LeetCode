#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        count = k
        value = -1
        def calculate(root):
            nonlocal count
            nonlocal value
            if root.left:
                calculate(root.left)
            count -= 1
            if count == 0:
                value = root.val
            if count <= 0:
                return
            if root.right:
                calculate(root.right)
        calculate(root)
        return value
            

        
# @lc code=end

