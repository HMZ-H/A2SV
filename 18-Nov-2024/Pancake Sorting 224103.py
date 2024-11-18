# Problem: Pancake Sorting - https://leetcode.com/problems/pancake-sorting/

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        
        flips = []

        for i in range(len(arr), 0, -1):
            index = arr.index(i)

            if index != i - 1:
                if index != 0:
                    arr[:index + 1] = reversed(arr[:index + 1])
                    flips.append(index + 1)
                    
                arr[:i] = reversed(arr[:i])
                flips.append(i)

        return flips