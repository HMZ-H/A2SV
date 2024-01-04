class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        cout = 0
        flip_sum = 0
        ind_sum = 0
        for i in range(len(flips)):
            ind_sum += i+1
            flip_sum += flips[i]
            if ind_sum == flip_sum:
                cout +=1
        return cout
        
        