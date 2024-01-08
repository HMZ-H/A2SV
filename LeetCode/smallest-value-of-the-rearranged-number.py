class Solution:
    def smallestNumber(self, num: int) -> int:
        # l = list(permutations(str(num)))
        # if num >0:
        #     res = [int(''.join(list(i)[::-1])) for i in l if len(str(int(''.join(list(i)[::-1])))) == len(str(num))]
        #     return min(res)
        # else:
        #     r = [int(''.join(i)) for i in l if '-'== i[0]]
        #     return min(r)

        if num == 0:
            return 0
        if num < 0:
            s = str(num)
            return - int(''.join(sorted(s[1:], reverse=True)))
        s = str(num)
        zero = 0
        lis = []

        for ind, chr in enumerate(s):
            if chr == '0':
                zero +=1
            else:
                lis.append(chr)

        lis.sort()
        return int(lis[0] + '0'*zero + ''.join(lis[1:]))        