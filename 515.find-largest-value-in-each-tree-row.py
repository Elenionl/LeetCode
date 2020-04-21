#
# @lc app=leetcode id=515 lang=python3
#
# [515] Find Largest Value in Each Tree Row
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        result = []
        def calculate(root, depth):
            if not root:
                return
            nonlocal result
            if len(result) <= depth:
                result.append(root.val)
            else:
                previous = result[depth]
                if previous < root.val:
                    result[depth] = root.val
            calculate(root.left, depth + 1)
            calculate(root.right, depth + 1)
        calculate(root, 0)
        return result
        
# @lc code=end

