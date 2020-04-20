#
# @lc app=leetcode id=501 lang=python3
#
# [501] Find Mode in Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        maxLength = 0
        previous = None
        currentLength = 0
        results = []
        def calculate(root):
            nonlocal previous
            nonlocal currentLength
            nonlocal results
            nonlocal maxLength
            if not root:
                return
            calculate(root.left)
            if root.val == previous:
                currentLength += 1
            else:
                currentLength = 1
            if currentLength == maxLength:
                results.append(root.val)
            elif currentLength > maxLength:
                results = [root.val]
                maxLength = currentLength
            previous = root.val
            calculate(root.right)
        calculate(root)
        return results

# @lc code=end

