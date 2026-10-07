# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # 3, 9 -> 5
        # 1, 9 -> 5
        # 2, 4 -> 3
        #assuming p> q
        #now address p <q
        if not root:
            return None
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif (root.val >= p.val and root.val <= q.val) or (root.val <= p.val and root.val >= q.val):
            return root