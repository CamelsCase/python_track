class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        out = [0]*len(s)
        ls = [0]*(len(s)+1)
        for i in shifts:
            op = -1 if i[2]==0 else 1
            ls[i[0]]+= op
            ls[i[1]+1]-=op
        ls=  list(accumulate(ls))[:-1]
        for ind,sh in enumerate(ls):
            out[ind]=((ord(s[ind])-97)+sh)%26
            out[ind] = chr(97+out[ind])
        return "".join(out) 