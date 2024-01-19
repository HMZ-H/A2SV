class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        occurr = {}
        max_len = 0
        left = 0
        for right in range(len(s)):
            char = s[right]
            if char in occurr and occurr[char] >= left:
                left = occurr[char] + 1
            else:
                max_len = max(max_len, right - left + 1)
            occurr[char] = right
        return max_len
        