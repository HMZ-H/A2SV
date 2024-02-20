class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        lis = path.split('/')
        for i in range(len(lis)):
            if  lis[i] == '..':
                if stack:

                    stack.pop()
            elif lis[i] not in ['.', '']:
                stack.append(lis[i])
        return '/'+'/'.join(stack)
            
        