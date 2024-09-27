# Problem: Recover a Tree From Preorder Traversal - https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        self.depth = 0
        self.i = 0
        def DFS(curr_depth):
            while self.i < len(traversal) and traversal[self.i] == "-":
                self.depth += 1
                self.i += 1
    
            if self.depth == curr_depth:
                val = ""
                while self.i < len(traversal) and traversal[self.i] != "-":
                    val += traversal[self.i]
                    self.i += 1

                root = TreeNode(int(val))
                self.depth = 0
                root.left = DFS(curr_depth + 1)
                root.right = DFS(curr_depth + 1)
                return root
            else:
                return None
        root = DFS(0)
        return root