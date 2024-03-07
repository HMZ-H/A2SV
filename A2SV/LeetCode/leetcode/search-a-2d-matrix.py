class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        arr = []
        for i in matrix:
            arr.extend(i)
        print(arr)
        left, right = 0, len(arr)-1
        flag = False
        while left<=right:
            mid = left + (right - left)//2
            print(mid, left, right)
            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid -1
            if arr[mid] == target:
                return True 
                break
        return False
            
