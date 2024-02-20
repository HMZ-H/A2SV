class Solution:    
    def decodeString(self, s: str) -> str:
        def rec( i , n,l):
            if  i >= len(s):
                return ""
            if s[i] == ']':
                l[0] = i
                return ""
            if s[i] == '[':
                return int(n)*rec(i+1, "", l) + rec(l[0]+1, "", l)
            if s[i].isdigit():
                return rec(i+1, n+s[i], l)
            else:
                return s[i] + rec(i+1, n, l)
        l = [0]
        return rec(0, "", l)
        # stack = []
        
        # num = 0
        # for i in s:
           
        #     if i != ']':
        #         stack.append(i)
        #     else:
        #         curr = []
        #         while stack and not stack[-1].isdigit():
        #             # val = []
        #             a = stack.pop()
        #             if a != '[':
        #                 curr.append(a)
        #         time = []
        #         while stack and  stack[-1].isdigit():
        #             time.append(stack.pop())
        #         time = int(''.join(time[::-1]))
        #         n = ''.join(curr[::-1])
        #         print(time,n,type(time),type(n))
        #         stack.append(self.rec(time, n))
        # res = []
        # for i in stack:
        #     res.append(i)
        # return ''.join(res)
                
        