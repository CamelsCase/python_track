class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vow = 0
        for i in s[:k]:
            if i in "aeiou":
                vow +=1
        mx = 0
        for i in range(1,len(s)-k+1):
            mx = max(vow,mx)
            if s[i-1]!=s[i+k-1]:
                if s[i-1]  in "aeiou":
                    vow-=1
                if s[i-1+k] in "aeiou":
                    vow+=1
        return max(mx,vow)