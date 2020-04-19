#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        result = []
        def calculate(root, previous):
            nonlocal result
            if not root:
                return
            
            if not root.left and not root.right:
                result.append(previous + str(root.val))
                return
            current = previous + str(root.val) + "->"
            calculate(root.left, current)
            calculate(root.right, current)
        calculate(root, "")
        return result
            
            



# @lc code=end

