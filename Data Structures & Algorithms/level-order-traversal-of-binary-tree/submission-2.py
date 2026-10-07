# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = deque()
        level = 0
        if root:
            q.append(root)
        while q:
            levelRes= []
            for i in range(len(q)):
                cur = q.popleft()
                levelRes.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            res.append(levelRes)
            level +=1
        return res
            
