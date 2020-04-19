#
# @lc app=leetcode id=113 lang=python3
#
# [113] Path Sum II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        if (not root.left) & (not root.right):
            if root.val == sum:
                return [[root.val]]
            else:
                return []
        left = self.pathSum(root.left, sum - root.val)
        right = self.pathSum(root.right, sum - root.val)
        result = left + right
        for item in result:
            item.insert(0, root.val)
        return result
# @lc code=end
