class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x = nums[:n]
        y = nums[n:]
        shuffle = []
        i = 0
        while n !=0:
            shuffle.append(x[i])
            shuffle.append(y[i])
            i +=1
            n-=1
        return shuffle
        