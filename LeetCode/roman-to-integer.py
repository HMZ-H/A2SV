class Solution:
    def romanToInt(self, s: str) -> int:
        maps = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        result, prev_value = 0, 0
        for i in reversed(s):
            current_value = maps[i]
            if current_value < prev_value:
                result -=current_value
            else:
                result += current_value
            prev_value = current_value
        return result

