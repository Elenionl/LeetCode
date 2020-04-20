#
# @lc app=leetcode id=404 lang=python3
#
# [404] Sum of Left Leaves
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        sum = 0
        def calculate(root, isLeft):
            nonlocal sum
            if not root:
                return
            if not root.left and not root.right and isLeft:
                sum += root.val
            calculate(root.left, True)
            calculate(root.right, False)
        calculate(root, False)
        return sum

        
# @lc code=end

