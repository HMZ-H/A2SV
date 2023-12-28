
class RandomizedSet:

    def __init__(self):
        self.dic = {}
        self.lis = []
        

    def insert(self, val: int) -> bool:
        if val in self.dic:
            return False
        
        self.dic[val] = len(self.lis)
        self.lis.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dic:
            return False
        if self.lis[-1] ==val:
            self.lis.pop()
            del self.dic[val]
        else:
            indx = self.dic[val]
            self.lis[-1],self.lis[indx] = self.lis[indx], self.lis[-1]
            self.dic[self.lis[indx]] = indx
            self.lis.pop()
            del self.dic[val]
        return True 

    def getRandom(self) -> int:
        return random.choice(self.lis)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()