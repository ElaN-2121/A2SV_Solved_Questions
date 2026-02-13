class FrequencyTracker:

    def __init__(self):
        self.count = defaultdict(int) # used to map a number with its respective count
        self.freq_count  = defaultdict(int) # A map to check how many numbers currently appear with that frequency: useful for hasFrequency() method

    def add(self, number: int) -> None:
        old_freq= self.count[number]

        if old_freq>0:
            self.freq_count[old_freq]-=1
        
        self.count[number] += 1
        new = self.count[number]

        self.freq_count[new] +=1

    def deleteOne(self, number: int) -> None:
        if self.count[number] == 0:
            return
        old_freq = self.count[number]
        self.freq_count[old_freq] -= 1

        self.count[number] -= 1
        new = self.count[number] 

        self.freq_count[new] += 1
        

    def hasFrequency(self, frequency: int) -> bool:
        return (self.freq_count[frequency] > 0)


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)
