class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        left = 0
        right = 0
        cout = []
        while left < len(nums1) and right < len(nums2):
            if nums1[left] == nums2[right]:
                cout.append(nums1[left])
                left +=1
                right +=1
            elif nums1[left] > nums2[right]:
                right +=1
            else:
                left +=1
        # cout.sort()
        if len(cout) != 0:
            return cout[0]
        return -1
            

        