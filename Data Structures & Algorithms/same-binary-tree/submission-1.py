# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, curr_p: Optional[TreeNode], curr_q: Optional[TreeNode]) -> bool:
        #traverse thru each node
        #
        if not curr_p and not curr_q:
            return True
        if not curr_p or not curr_q:
            return False
        if curr_p.val != curr_q.val:
            return False
        return self.isSameTree(curr_p.left, curr_q.left) and self.isSameTree(curr_p.right, curr_q.right)
            
