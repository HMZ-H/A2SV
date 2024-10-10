# Problem: Keyboard Row - https://leetcode.com/problems/keyboard-row/description/

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        keyboard_row = ["qwertyuiop","asdfghjkl", "zxcvbnm"]
        res = []
        for word in words:
            if all(char in keyboard_row[0] for char in word.lower()) or all(char in keyboard_row[1] for char in word.lower()) or all(char in keyboard_row[2] for char in word.lower()):
                
                res.append(word)
        return res