class Solution:
    def maxVowels(self, s: str, k: int) -> int:
    #     max_vowel = 0
    #     left, right = 0, k
    #     if len(s) == 0:
    #         return 0
    #     while right <= len(s):
    #         sub_arr = s[left:right]
    #         cout_a = sub_arr.count('a')
    #         cout_e = sub_arr.count('e')
    #         cout_i = sub_arr.count('i')
    #         cout_o = sub_arr.count('o')
    #         cout_u = sub_arr.count('u')
    #         total = cout_a + cout_e + cout_i + cout_o + cout_u
    #         max_vowel = max(max_vowel, total)
    #         left +=1
    #         right +=1
    #     return max_vowel

    #     class Solution:
    # def maxVowels(self, s: str, k: int) -> int:
        s = list(s)
        vowels = ['a','e','i','o','u']
        window = s[:k]
        cout_vowel = [e for e in window if e in vowels]
        max_v = len(cout_vowel)
        curre_v = max_v

        for i in range(k, len(s)):
            if s[i-k] in vowels:
                curre_v -= 1
            if s[i] in vowels:
                curre_v += 1
            if curre_v > max_v:
                max_v = curre_v
        return max_v
        
        