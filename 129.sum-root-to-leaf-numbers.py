#
# @lc app=leetcode id=129 lang=python3
#
# [129] Sum Root to Leaf Numbers
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        def calculate(root):
            if not root:
                return []
            if (not root.left) and (not root.right):
                return [[root.val]]
            left = calculate(root.left)
            right = calculate(root.right)
            total = left + right
            for item in total:
                item.append(root.val)
            return total
        result = calculate(root)
        resultNumber = 0
        for line in result:
            local = 0
            while line:
                value = line.pop()
                local = local * 10 + value
            resultNumber += local
        return resultNumber
            

# @lc code=end

