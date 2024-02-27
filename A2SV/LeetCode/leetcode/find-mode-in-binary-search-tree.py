# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        lis = []
        def inor(root):
            if root:
                root.left = inor(root.left)
                lis.append(root.val)
                root.right = inor(root.right)
        inor(root)
        print(lis)
        fre = Counter(lis)
        res = []
        max_ = max(fre.values())
        for key, val in fre.items():
            if val == max_:
                res.append(key)
        print(res)
    
        return res

        