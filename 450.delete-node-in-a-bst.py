#
# @lc app=leetcode id=450 lang=python3
#
# [450] Delete Node in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return root
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            
            
            pre = root
            nex = root.right
            while nex.left:
                pre = nex
                nex = nex.left
	    	# Get the leftmost child of the right node of root
	    	# Also keep the pre/parent in that path
    
            root.val = nex.val # Replace root val with nex/leftmost node's val
            if pre != root: # If root's right had a left child
                pre.left = nex.right
            else:
                pre.right = nex.right # If root's right had no left child
    
        return root



# @lc code=end

