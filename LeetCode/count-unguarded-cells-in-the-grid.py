class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        walls_set = {(x,y) for x,y in walls}
        guards_set = {(x, y ) for x,y in guards}
        unguard = set()
        len_guard = 0
        len_guard_point = 0
        for x,y in guards:
            len_guard +=1
            # Go to up
            for i in range(x-1, -1, -1):
                if (i, y) in guards_set or (i, y) in walls_set:
                    break
                elif (i, y) in unguard:
                    continue
                    
                else:
                    unguard.add((i, y))
                    len_guard_point +=1 
            # Go down
            for i in range(x+1, m):
                if (i, y) in guards_set or (i, y) in walls_set:
                    break
                elif (i, y) in unguard:
                    continue
                else:
                    unguard.add((i, y))
                    len_guard_point +=1
            # Go to right
            for i in range(y+1, n):
                if (x, i) in guards_set or (x, i ) in walls_set:
                    break 
                elif (x, i) in unguard:
                    continue
                else:
                    unguard.add((x,i))
                    len_guard_point +=1
            # go to left
            for i in range(y-1, -1, -1):
                if (x, i) in guards_set or (x, i) in walls_set:
                    break
                elif (x, i) in unguard:
                    continue
                else:
                    unguard.add((x,i))
                    len_guard_point +=1
        total_grid = n*m
        total_guarded = len_guard + len(walls_set) + len_guard_point
        return total_grid - total_guarded
         

        