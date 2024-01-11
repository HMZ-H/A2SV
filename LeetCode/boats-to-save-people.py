class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = 0
        right = len(people)-1
        cout = 0
        while right>= left:
            if people[left] + people[right] <= limit:
                left +=1
            right -=1
            cout +=1
        return cout
            

        