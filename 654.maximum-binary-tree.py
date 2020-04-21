#
# @lc app=leetcode id=654 lang=python3
#
# [654] Maximum Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        maxValue = max(nums)
        maxIndex = nums.index(maxValue)
        left = self.constructMaximumBinaryTree(nums[0:maxIndex])
        right = self.constructMaximumBinaryTree(nums[maxIndex + 1:])
        node = TreeNode(maxValue)
        node.left = left
        node.right = right
        return node
# @lc code=end

