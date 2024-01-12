class Solution:
    def sortSentence(self, s: str) -> str:
        x = s.split()
        x.sort(key =lambda a:int(a[-1]))
        for i in range(len(x)):
            x[i] = x[i][:-1]
        return " ".join(x)
