# Problem: Balanced Binary Tree - https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        lst = set()
        if not root:
            return True
        def rec(node,c):
            if not node:
                c-=1
                return c
            left,right = c,c
            left = rec(node.left,c+1)
            right = rec(node.right,c+1)
            if abs(left - right)>1:
                lst.add(False)
            return max(left,right)
        rec(root,0)
        
        return not False in lst