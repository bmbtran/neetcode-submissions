# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: 
    def sameTree(self,r, t):
        if not r and not t:
            return True
        if not r or not t:
            return False
        if r.val == t.val:
            return self.sameTree(r.left, t.left) and self.sameTree(r.right, t.right)
        else:
            return False  
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #DFS
        #recursive
        
        #same structure AND same values -> TRUE
        #if (root and (not subRoot)) or (subRoot and (not root)):
        #return False
        #for every node, if node.val == subroot.val
        #dfs(node.left, subroot.left)
        #dfs(node.right, subroot.right)
        #return True

        #base case:

        #base case:
        if not root:
            return False
        if not subRoot:
            return True
        if self.sameTree(root,subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


