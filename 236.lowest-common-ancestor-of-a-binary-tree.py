#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = [root]
        index = {root: None}
        while p not in index or q not in index:
            item = stack.pop()
            if item.left:
                stack.append(item.left)
                index[item.left] = item
            if item.right:
                stack.append(item.right)
                index[item.right] = item
        ancestors = []
        while p:
            ancestors.append(p)
            p = index[p]
        while q not in ancestors:
            q = index[q]
        return q
# @lc code=end

