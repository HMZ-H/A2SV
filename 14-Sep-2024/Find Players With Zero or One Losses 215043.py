# Problem: Find Players With Zero or One Losses - https://leetcode.com/problems/find-players-with-zero-or-one-losses

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win = set()
        los = defaultdict(int)
        for i in matches:
            win.add(i[0])
            los[i[1]] +=1
        z = [i for i in win if i not in los]
        o = [i for i in los if los[i] ==1]
        return [sorted(z), sorted(o)]


        