#
# @lc app=leetcode id=623 lang=python3
#
# [623] Add One Row to Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if not root:
            return
        if d == 1:
            node = TreeNode(v)
            node.left = root
            return node
        if d == 2:
            left = root.left
            right = root.right
            root.left = TreeNode(v)
            root.left.left = left
            root.right = TreeNode(v)
            root.right.right = right
            return root
        self.addOneRow(root.left, v, d - 1)
        self.addOneRow(root.right, v, d - 1)
        return root
        
# @lc code=end

