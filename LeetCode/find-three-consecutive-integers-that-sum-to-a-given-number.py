class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        temp = int(num/3)
        res = ((temp-1) + temp + (temp+1))
        return [temp-1, temp, temp+1] if res == num else []
        