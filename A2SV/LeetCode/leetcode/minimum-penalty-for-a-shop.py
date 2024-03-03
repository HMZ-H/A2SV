class Solution:
    def bestClosingTime(self, customers: str) -> int:
        # Prefix sum of customers 
        prefix_n = [0]
        for i in customers:
            if i == 'N':
                prefix_n.append(prefix_n[-1] + 1)
            else:
                prefix_n.append(prefix_n[-1])
        # Postfix sum of customers
        postfix_y = [0]
        for i in range(len(customers)-1, -1,-1):
            if customers[i] == 'Y':
                postfix_y.append(postfix_y[-1] +1)
            else:
                postfix_y.append(postfix_y[-1])
        postfix_y = postfix_y[::-1]
        # Checking for earliyer index for closing
        res = float('inf')
        ind = 0
        for i in range(len(postfix_y)):
            temp = postfix_y[i] + prefix_n[i]
            if temp < res:
                res = temp
                ind = i
         
        return ind

        