class ATM:

    def __init__(self):
        self.notes =[20, 50, 100, 200, 500]
        self.count = [0]*5
        

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(len(banknotesCount)):
            self.count[i] += banknotesCount[i]
        

    def withdraw(self, amount: int) -> List[int]:
        res = [0]*5
        total = 0
        for i in range(len(self.notes)-1,-1,-1):
            used = min(amount//self.notes[i], self.count[i])
            res[i] = used
            total += used * self.notes[i]
            amount -= used * self.notes[i]

        if amount != 0:
            return [-1]

        for i in range(len(self.notes)):
            self.count[i] -= res[i]
        return res
        
        


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)