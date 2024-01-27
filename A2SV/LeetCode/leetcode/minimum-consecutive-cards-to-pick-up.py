class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        fre=defaultdict(int)
        min_=float("inf")
        for right in range(len(cards)):
            if cards[right] not in fre:
                fre[cards[right]]=right
            else:
                min_=min(min_,right-fre[cards[right]]+1)
                fre[cards[right]]=right
        if min_==float("inf"):
            return -1
        else:
            return min_

        