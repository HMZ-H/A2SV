class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        opens = 0
        closes = 0
        stack = []
        for char in s:
            if stack and stack[-1] == '('and char == ')':
                stack.pop()
            else:
                stack.append(char)

        # print(len(stack))
        return len(stack)

        