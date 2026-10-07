# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # if root is None or root.left is None or root.right is None:
        #     return False
        # if root.val > root.left.val and root.val < root.right.val:
        #     return True
        # if self.isValidBST(root.left) and self.isValidBST(root.right):
        #     return True
        # else:
        #     return False

        def isValid(node, low, high):
            if not node:
                return True
            if not node.val > low or not node.val < high:
                return False
            return isValid(node.left, low, node.val) and isValid(node.right, node.val, high)


        return isValid(root, float("-inf"), float("inf"))