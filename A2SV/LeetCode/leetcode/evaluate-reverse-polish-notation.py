class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operator = ['+', '-', '*', '/']
        for num in tokens:
            if num not in operator:
                stack.append(int(num))
            elif num in operator:
                a = stack.pop()
                b = stack.pop()
                if num == '+':
                    stack.append(a + b)
                elif num == '-':
                    stack.append(b-a)
                elif num == '/':
                    stack.append(int(b/a))
                elif num == '*':
                    stack.append(a * b)


                # print(operator[num](int(a),int(b)))
        print(stack)
        return stack[0]

        