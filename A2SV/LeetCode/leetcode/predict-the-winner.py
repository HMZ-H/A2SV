class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def rec(left, right, player1, player2, turn = True):
            if left > right:
                return player1 >= player2
            if turn:
                return rec(left+1, right, player1 + nums[left],player2, not turn) \
                or rec(left, right -1, player1 + nums[right], player2, not turn)
            else:
                return rec(left+1, right, player1, player2 + nums[left], not turn)\
                and rec(left, right-1, player1, player2 + nums[right], not turn)
        return rec(0, len(nums)-1, 0, 0, True)
        #    
        
        