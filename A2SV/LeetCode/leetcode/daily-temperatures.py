class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0]*len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while stack and stack[-1][0]<temperatures[i]:
                x =  stack.pop()
                res[x[1]] = i - x[1]
          
            stack.append([temperatures[i], i]) 

        return res
        