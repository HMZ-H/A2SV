class FrequencyTracker:

    def __init__(self):
        self.fre =  Counter()
        self.num = Counter()

    def add(self, number: int) -> None:
        prev = self.num[number]
        self.num[number] +=1
        self.fre[prev] -=1
        self.fre[prev + 1] +=1
        

    def deleteOne(self, number: int) -> None:
        prev = self.num[number]
        if prev == 0:
            return
        
        self.num[number] -=1
        self.fre[prev] -=1
        self.fre[prev -1] +=1

        

    def hasFrequency(self, frequency: int) -> bool:
        return self.fre[frequency] >= 1
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)