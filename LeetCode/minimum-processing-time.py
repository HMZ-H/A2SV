class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse=True)
        
        time = []
        l = 0

        for i in range(len(processorTime)):
            time.append(processorTime[i] + tasks[l])
            l +=4

           
        return max(time)        