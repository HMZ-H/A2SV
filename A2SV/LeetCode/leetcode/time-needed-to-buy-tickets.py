class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        que = deque([i for i in range(len(tickets))])
        time = 0
        while que:
            for i in range(len(que)):
                poped = que.popleft()
                tickets[poped] -= 1
                if tickets[poped] >=1:
                    que.append(poped)
                time +=1
                if tickets[k] == 0:
                    return time 


        