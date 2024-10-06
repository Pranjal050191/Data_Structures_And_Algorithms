# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root) -> bool:
        def validate(node, low, high):
            # An empty tree is a valid BST
            if not node:
                return True
            
            # The current node's value must be between low and high
            if node.val <= low or node.val >= high:
                return False
            
            # Recursively check the left subtree with updated high boundary
            # and the right subtree with updated low boundary
            return validate(node.left, low, node.val) and validate(node.right, node.val, high)
        
        # We start with the whole range of valid values (-infinity to +infinity)
        return validate(root, float('-inf'), float('inf'))
    

#      32
#     /  \
#    26   47
#   /      \
# 19        56
#  \
#   27