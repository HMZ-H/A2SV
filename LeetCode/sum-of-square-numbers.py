class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # lis = [i for i in range(0, c+1)]

       
        # for i in range(c+1):
        left, right = 0, floor(sqrt(c))
        while left <= right:
            if left**2 + right**2 > c:
                right -=1
                
            elif left**2 + right**2 == c:
                return True
            else:
                left +=1
        #     # print(lis[left]**2, lis[right]**2)

           

        # for i in range(len(lis)):
        #     for j in range(len(lis)):
        #         if lis[i]**2 + lis[j]**2 ==c:
        #             return True
        return False

        