#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        center = preorder[0]
        centerIndex = inorder.index(center)
        leftPreorder = preorder[1:(centerIndex + 1)]
        leftInorder = inorder[0:centerIndex]
        rightPreorder = preorder[(centerIndex + 1):]
        rightInorder = inorder[(centerIndex + 1):]
        node = TreeNode(center)
        node.left = self.buildTree(leftPreorder, leftInorder)
        node.right = self.buildTree(rightPreorder, rightInorder)
        return node

# @lc code=end

