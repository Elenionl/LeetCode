#
# @lc app=leetcode id=95 lang=python3
#
# [95] Unique Binary Search Trees II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def generateTree(fromValue: int, toValue: int) -> List[TreeNode]:
            if fromValue == toValue:
                return []
            result = []
            if fromValue == toValue - 1:
                return [TreeNode(fromValue)]
            for i in range(fromValue, toValue):
                left = generateTree(fromValue, i)
                right = generateTree(i + 1, toValue)
                if not right:
                    for leftElement in left:
                        node = TreeNode(i)
                        node.left = leftElement
                        result.append(node)
                elif not left:
                    for rightElement in right:
                        node = TreeNode(i)
                        node.right = rightElement
                        result.append(node)
                else:
                    for rightElement in right:
                        for leftElement in left:
                            node = TreeNode(i)
                            node.right = rightElement
                            node.left = leftElement
                            result.append(node)
            return result
        return generateTree(1, n + 1)
                
        
# @lc code=end

