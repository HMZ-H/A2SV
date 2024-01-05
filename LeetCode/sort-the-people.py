class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
     
        # for i in range(len(names)):
        #     max_ = i
        #     for j in range(i,len(names)):
                
        #         if heights[max_] < heights[j]: 
        #             max_ = j
        #     heights[max_], heights[i] = heights[i], heights[max_]
        #     names[max_], names[i] = names[i], names[max_]
        # return names
        for i in range(1, len(names)):
            j = i -1
            curr_val = heights[i]
            curr_name = names[i]
            while j >= 0 and curr_val > heights[j]:
                heights[j+1] = heights[j]
                names[j+1] = names[j]
                j -=1
            j +=1
            if j != i:
                heights[j] = curr_val
                names[j] = curr_name
        return names

        
       