# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def dfs(l,r):
            if l > r:
                return
            max_ = float('-inf')
            ind = 0
            for i in range(l, r+1):
                if nums[i] > max_:
                    max_ = nums[i]
                    ind = i

            # max_ = max(nums[l:r+1])
            root = TreeNode(max_)
            root.left = dfs(l, ind-1)
            root.right = dfs(ind+1, r)
            return root
        return dfs(0, len(nums)-1)


        