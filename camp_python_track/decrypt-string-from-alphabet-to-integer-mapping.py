class Solution:
    def freqAlphabets(self, s: str) -> str:
        m = {}
        for i in range(1,27):
            if i <=9:
                m[f'{i}'] = chr(ord("a")+i-1)
            else:
                m[f'{i}#'] = chr(ord("j")+i-10)
        s = s[::-1]
        out = ""
        i = 0
        while True:
            if i==len(s):
                break
            if s[i] != "#":
                out+=m[s[i]]
                i+=1
            elif s[i] == "#":
                out+=m[s[i:i+3][::-1]]
                i+=3
        return out[::-1]