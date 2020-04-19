#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.

from typing import List


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
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
        return result



# @lc code=end
