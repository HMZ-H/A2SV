class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
      
       lis = [[position[i], speed[i]] for i in range(len(speed))]
       lis.sort(key = lambda x: -x[0])
       stack = [0]
       for i in range(len(lis)):
           diff = (target - lis[i][0])/lis[i][1]
           if diff > stack[-1]:
               stack.append(diff)
       return len(stack)-1
        