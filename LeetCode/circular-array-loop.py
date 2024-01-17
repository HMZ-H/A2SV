class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        # fre = Counter(nums)
        # for key, value in fre.items():
        #     if value >= 2:
        #         return True
        #     else:
        #         return False
        n = len(nums)
        check = set()
        for i in range(n):
            if i not in check:
                cycle_set = set()

                while True:
                    if i in cycle_set:
                        return True
                    

                    check.add(i)
                    cycle_set.add(i)
                    prev, i = i, (i + nums[i])%n
                    
                    if prev == i:
                        break
                    
                    if  nums[prev] > 0 != nums[i] < 0:
                        break
        return False

                    