# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        # res = 0
        def dfs(root, p, q):
            if not root:
                return 
            if root:
                # if p greater than root or p less than root
                if p.val < root.val and q.val > root.val or p.val > root.val and q.val < root.val:
                    return root
                #
                if p.val == root.val and (q.val > root.val or q.val < root.val):
                    return root

                if q.val == root.val and (p.val > root.val or p.val < root.val) :
                    return root
          
                return dfs(root.left, p, q) or dfs(root.right, p, q)
        return dfs(root, p, q)

                
        
