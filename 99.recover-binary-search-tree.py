#
# @lc app=leetcode id=99 lang=python3
#
# [99] Recover Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        first = None
        second = None
        previous = None
        def recover(root: TreeNode):
            nonlocal second
            nonlocal previous
            nonlocal first
            if not root:
                return
            recover(root.left)
            if not previous:
                previous = root
            elif root.val <= previous.val:
                if not first:
                    first = previous
                    second = root
                    previous = root
                else:  
                    second = root
            else:
                previous = root
            recover(root.right)
        recover(root)
        tmp = second.val
        second.val = first.val
        first.val = tmp
        return root

        
# @lc code=end

