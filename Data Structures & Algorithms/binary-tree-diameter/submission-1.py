# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #maxLeft + maxRight
        highest = 0
        def dfs(node): 
            nonlocal highest
            if not node:
                return 0
            heightLeft = dfs(node.left)
            heightRight = dfs(node.right)
            highest = max(highest, heightLeft + heightRight)
            return 1+ max(heightLeft, heightRight)
        dfs(root)
        return highest