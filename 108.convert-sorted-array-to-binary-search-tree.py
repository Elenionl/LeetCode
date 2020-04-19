#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        middleIndex = (len(nums) - 1) // 2
        node = TreeNode(nums[middleIndex])
        node.left = self.sortedArrayToBST(nums[0:middleIndex])
        node.right = self.sortedArrayToBST(nums[(middleIndex + 1):])
        return node
# @lc code=end

