class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for i in words:
            leng = len(i)
            found = True
            for j in range(leng//2):
                if i[j]!=i[len(i)-1-j]:
                    found  = False
                    break
            if found:
                return i
        return ""
                    