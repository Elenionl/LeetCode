#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        result = []
        def calculate(root):
            nonlocal result
            if root:
                result.append(str(root.val))
                calculate(root.left)
                calculate(root.right)
            else:
                result.append("#")
        calculate(root)
        return " ".join(result)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        values = iter(data.split(" "))
        def calculate():
            nonlocal values
            value = next(values)
            if value == "#":
                return None
            node = TreeNode(int(value))
            node.left = calculate()
            node.right = calculate()
            return node
        return calculate()
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
# @lc code=end

