class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        # candies = [4,2,1,1,2]
        # extraCandies = 1
        greatest_= max(candies)
        result = []
        for i in candies:
            if i + extraCandies >= greatest_:
                result.append(True)
            else:
                result.append(False)
        return result
        