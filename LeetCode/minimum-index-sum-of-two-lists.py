class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index_sum = {}
        res = []

        for i, word in enumerate(list1):
            index_sum[word] = i

        min_sum = float('inf')
        for j, word in enumerate(list2):
            if word in index_sum:
                curr_sum = j + index_sum[word]
                if curr_sum < min_sum:
                    res = [word]
                    min_sum = curr_sum
                elif curr_sum == min_sum:
                    res.append(word)
        return res
        
        
