class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        curr = self.getMin()
        if val < curr:
            curr = val
        self.stack.append((val, curr))
        

    def pop(self) -> None:
        x = self.stack[-1][0]
        # self.stack.pop
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        if not self.stack:
            return float('inf')
        return self.stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()