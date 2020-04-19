#
# @lc app=leetcode id=106 lang=python3
#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not postorder:
            return None
        center = postorder[-1]
        centerIndex = inorder.index(center)
        leftPostorder = postorder[0:centerIndex]
        leftInorder = inorder[0:centerIndex]
        rightPostorder = postorder[centerIndex: -1]
        rightInorder = inorder[(centerIndex + 1):]
        node = TreeNode(center)
        node.left = self.buildTree(leftInorder, leftPostorder)
        node.right = self.buildTree(rightInorder, rightPostorder)
        return node
# @lc code=end

