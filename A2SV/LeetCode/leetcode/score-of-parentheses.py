class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        cout = 0
        for i in s:
            if i == '(':
                stack.append(0)
            else:
                remo = stack.pop()
                stack[-1] += max(2*remo, 1)
        return stack[-1]
           
        return cout

            

        