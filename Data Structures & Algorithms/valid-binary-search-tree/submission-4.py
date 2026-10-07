# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValidSubTree(node, minAllowed, maxAllowed):
            if not node:
                return True
            if minAllowed < node.val < maxAllowed:
                return isValidSubTree(node.left, minAllowed, node.val) and isValidSubTree(node.right, node.val, maxAllowed)
            else:
                return False
        return isValidSubTree(root, float('-inf'), float('inf'))

        
