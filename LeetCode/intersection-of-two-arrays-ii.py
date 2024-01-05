class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        fre1 = Counter(nums1)
        fre2 = Counter(nums2)

        res = []

        for i in fre1:
            if fre2.get(i) is not None:
                res.extend(min(fre1[i], fre2[i])*[i])
        return res
        