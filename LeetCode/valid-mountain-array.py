class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) <= 2 or max(arr) == arr[0] or max(arr) == arr[len(arr)-1]:
            return False
        valid = True
        for i in range(len(arr)-1):
            if valid and arr[i] >= arr[i+1]:
                valid = False
            if not valid  and arr[i] <= arr[i+1]:
                return False

        return True
        