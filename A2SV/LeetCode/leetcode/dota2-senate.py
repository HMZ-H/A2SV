class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        que = deque(senate)
        rRadiant = 0
        dDire = 0
        for i in senate:
            if i == 'D':
                dDire +=1

            else:
                rRadiant +=1
        removedDire = removedRadiant = 0
        while True:
            if dDire == 0:
                return "Radiant"
            elif rRadiant == 0:
                return 'Dire'
            vote = que.popleft()
            if vote == 'D':
                if removedDire >0:
                    removedDire -=1
                    dDire -=1
                else:
                    removedRadiant +=1
                    que.append(vote)
            else:
               
                if removedRadiant >0:
                    removedRadiant -=1
                    rRadiant -=1
                else:
                    removedDire +=1
                    que.append(vote)
            
                
                




        