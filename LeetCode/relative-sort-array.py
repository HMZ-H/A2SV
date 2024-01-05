class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:

        fre = Counter(arr1)
        lis = []
        not_appear = []
        for i in arr2:
            lis.extend([i]*fre[i])
        for i in arr1:
            if i not in arr2:
                not_appear.append(i)
        not_appear.sort()
        lis.extend(not_appear)

        return lis 
        