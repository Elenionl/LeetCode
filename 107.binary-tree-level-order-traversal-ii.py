#
# @lc app=leetcode id=107 lang=python3
#
# [107] Binary Tree Level Order Traversal II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        queue = []
        queue.append([root])
        result = []
        while queue:
            next_queue = []
            current_result = []
            for node in queue.pop(0):
                if node:
                    current_result.append(node.val)
                    if node.left:
                        next_queue.append(node.left)
                    if node.right:
                        next_queue.append(node.right)
            if current_result:
                queue.append(next_queue)
                result.append(current_result)
        return reversed(result)
# @lc code=end

