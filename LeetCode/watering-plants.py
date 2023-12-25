class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        step = 0
        cap = capacity
        for i in range(len(plants)):
            step +=1
            if plants[i]>cap:
                step +=2*i
                cap=capacity

            cap -= plants[i]
        return step
        