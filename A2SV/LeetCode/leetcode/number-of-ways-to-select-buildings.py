class Solution:
    def numberOfWays(self, s: str) -> int:
        total_zeros = 0
        total_ones = 0
        for i in s:
            if i == '0':
                total_zeros +=1
            else:
                total_ones +=1
        zeros_seen = 0
        ones_seen = 0
        cout = 0
        for i in s:
            if i == '0':
                cout += (total_ones - ones_seen)*ones_seen
                zeros_seen +=1
            else:
                cout += (total_zeros - zeros_seen)*zeros_seen
                ones_seen +=1
        # print(zeros_seen, ones_seen, cout)
        return cout

                

        

        