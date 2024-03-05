# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        lis = []

        def div_conqur(start, ends):
            mid = (start + ends)//2
            if start == ends:
                return TreeNode(nums[mid])
            if start > ends:
                return 
            root=TreeNode(nums[mid])
            root.left = div_conqur(start, mid-1)
            root.right = div_conqur(mid +1, ends)
            return root
        
        return div_conqur(0, len(nums)-1)
        
        
        
        


        