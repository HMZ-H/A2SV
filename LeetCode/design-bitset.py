class Bitset:

    # def __init__(self, size: int):
    #     self.lookup = defaultdict(int)
    #     self.total = 0
    #     self.n = size
    #     self.flipped = False
        
    #  # set to 0
    # def fix(self, idx: int) -> None:
    #     prev = self.lookup[idx]
    #     if self.flipped:
    #         self.lookup[idx] = 0

    #         if prev != 0:
    #             self.total -=1
    #     else:
    #         self.lookup[idx] = 1
    #         if prev != 1:
    #             self.total += 1
             
    # #set to 1
    # def unfix(self, idx: int) -> None:
    #     prev = self.lookup[idx]
    #     if self.flipped:
    #         self.lookup[idx] = 1
    #         if prev !=1:
    #             self.total +=1
    #     else:
    #         self.lookup[idx] = 0
    #         if prev !=0:
    #             self.total -=1

    # def flip(self) -> None:
    #     self.flipped = not self.flipped
        
   
    # def all(self) -> bool:
    #     if self.flipped:
    #         return self.total == 0
    #     else:
    #         return self.total == self.n

        

    # def one(self) -> bool:
    #     if self.flipped:
    #         return self.total < self.n
    #     else:
    #         return self.total > 0
        

    # def count(self) -> int:
    #     if self.flipped:
    #         return self.n - self.total
    #     else:
    #         return self.total
        

    # def toString(self) -> str:
    #     res = []
    #     for size in range(self.n):
    #         b = self.lookup[size]
    #         if self.flipped:
    #             b = 1 - b
    #             res.append(b)

    #     return "".join(str(x) for x in res)
    def __init__(self, size: int):
        self.lookup = defaultdict(int)
        self.total = 0
        self.n = size
        self.flipped = False

    def fix(self, idx: int) -> None:

        prev = self.lookup[idx]
        if self.flipped:
            self.lookup[idx] = 0
            if prev != 0:
                self.total -= 1
        else:
            self.lookup[idx] = 1
            if prev != 1:
                self.total += 1

    def unfix(self, idx: int) -> None:
        prev = self.lookup[idx]
        if self.flipped:
            self.lookup[idx] = 1
            if prev != 1:
                self.total += 1
        else:
            self.lookup[idx] = 0
            if prev != 0:
                self.total -= 1

    def flip(self) -> None:
        self.flipped = not self.flipped

    def all(self) -> bool:
        if self.flipped:
            return self.total == 0
        else:
            return self.total == self.n

    def one(self) -> bool:
        if self.flipped:
            return self.total < self.n
        else:
            return self.total > 0

    def count(self) -> int:
        if self.flipped:
            return self.n - self.total
        else:
            return self.total

    def toString(self) -> str:
        res = [str(1 - self.lookup[size]) if self.flipped else str(self.lookup[size]) for size in range(self.n)]

        return "".join(res)

        


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()