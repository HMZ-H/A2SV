class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count = 0
        for i in range(k):
            count += blocks[i] == 'W'
        result = count
        left, right = 0, k

        while right < len(blocks):
            count -= blocks[left] == 'W'
            count += blocks[right] == 'W'
            result = min(result, count)
            left +=1
            right +=1

        return result