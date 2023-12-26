class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        # lis = []
        # for i in queries:
        #     nums[i[1]] += i[0]
        #     even = 0
        #     for i in nums:
        #         if i%2==0:
        #             even+=i
        #     lis.append(even)
        # return lis
        sm=0
        for i in range(len(nums)):
            if nums[i]%2==0:
                sm+=nums[i]
        lst=[]
        for i in range(len(queries)):
            prev=nums[queries[i][1]]
            nums[queries[i][1]]+=queries[i][0]
            curr=nums[queries[i][1]]
            if prev%2==0:
                if curr%2==0:
                    sm+=(curr-prev)
                else:
                    sm-=prev
            else:
                if curr%2==0:
                    sm+=curr
            lst.append(sm)
        return lst
        