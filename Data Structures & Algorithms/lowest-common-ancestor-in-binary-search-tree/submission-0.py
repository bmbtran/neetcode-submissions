# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #edge case:
        # [5,3,8,1,4,7,9,null,2] p = 3, q = 5 -> return 5 
        #[5,3,8,1,4,7,9,null,2] p = 3, q =1 -> return 3
        #clarifying questions: are p and q guaranteed to exist in the BST?
        #if p and q both left or both right (smaller than 5), call recursive on that subtree 
        #if p and q on left vs right or p or q is root-> then descendant of root/cur
        #traverse through each node
        #store curr node being traversed: 5
        #compare p and q with 5, p < 5 -> go to the left. q > 5-> search right
        #dfs
        if not root:
            return None
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p,q)
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p,q)
        else:
            return root



