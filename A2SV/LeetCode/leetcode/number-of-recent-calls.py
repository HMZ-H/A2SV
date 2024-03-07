class RecentCounter:

    def __init__(self):
        self.cout = 0
        self.lis = []
        
    def ping(self, t: int) -> int:
        self.lis.append(t)
        while (t- self.lis[0] )> 3000:
            self.lis.pop(0)
        return len(self.lis)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)