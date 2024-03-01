# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(root, min_, max_):
            nonlocal res
            if not root:
                return
            min_ = min(min_, root.val)
            max_ = max(max_, root.val)
            res = max(res, abs(min_ - max_))
            dfs(root.left, min_, max_)
            dfs(root.right, min_, max_)
        dfs(root, root.val, root.val)
        return res

            
            

        