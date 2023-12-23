class FrequencyTracker:
    def __init__(self):
        self.freq = Counter()
        self.freq2 = Counter()
    def add(self, number: int) -> None:
        self.freq[number]+=1
        self.freq2[self.freq[number]-1]-=1
        self.freq2[self.freq[number]]+=1
        # print("this is the out for add")
        # print(self.freq)
        # print(self.freq2)
            

    def deleteOne(self, number: int) -> None:
        if self.freq[number]:
            self.freq[number] -=1
            if self.freq[number]==0:
                del self.freq[number]

            self.freq2[self.freq[number]]+=1
            self.freq2[self.freq[number]+1]-=1
        # print("this is the out for delete")
        # print(self.freq)
        # print(self.freq2)
            

    def hasFrequency(self, frequency: int) -> bool:
        # print("this is the out for freq")
        # print(self.freq)
        # print(self.freq2)
        return  self.freq2[frequency]>0

# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)