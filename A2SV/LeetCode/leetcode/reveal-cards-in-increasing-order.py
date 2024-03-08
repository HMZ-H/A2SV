class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        q  = deque()
        while deck:
            x = deck.pop()
            if len(q)>=2:
                q.appendleft(q.pop())
            q.appendleft(x)
        return q