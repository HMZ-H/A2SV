# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        mid = n//2
        right = n
        left = 1
        while left <= right:
            if isBadVersion(mid):
                right = mid -1
                # mid = right//2
            else:
                left = mid +1
            mid = (right + left)//2
        return mid+1
        