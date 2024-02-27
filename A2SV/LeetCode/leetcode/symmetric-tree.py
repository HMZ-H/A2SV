# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def helper(left,right):
            if not right and not left:
                return True
            if not right or not left:
                return False
            
            lef= helper(left.left,right.right)
            rig=helper(left.right,right.left)
            return  left.val==right.val and lef and rig
        return helper(root.left,root.right)
     
       
    


