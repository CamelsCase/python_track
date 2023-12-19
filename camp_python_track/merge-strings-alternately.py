class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        out = ''
        l1 = len(word1)
        l2 = len(word2)
        if l1>=l2:
            for i in range(l2):
                out+=word1[i]+word2[i]
            out+=word1[l2:]
        elif l1<l2:
            for i in range(l1):
                out+=word1[i]+word2[i]
            out+=word2[l1:]
        return out