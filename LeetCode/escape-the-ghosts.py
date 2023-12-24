class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        pac_man_dis = abs(target[0]) + abs(target[1])
        for ghost in ghosts:
            ghost_dis = abs(target[0] - ghost[0]) + abs(target[1] - ghost[1])
            if pac_man_dis >= ghost_dis:
                return False
        return True