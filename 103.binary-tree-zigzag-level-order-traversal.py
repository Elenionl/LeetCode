#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = []
        queue.append([root])
        result = []
        index: int = 0
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
                if index % 2 != 0:
                    current_result = reversed(current_result)
                result.append(current_result)
            index = index + 1
        return result
# @lc code=end

