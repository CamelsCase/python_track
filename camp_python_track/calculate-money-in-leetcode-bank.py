class Solution:
    def totalMoney(self, n: int) -> int:
        out = 0
        lm = 0
        flag = False
        for i in range(ceil(n/7)):
            s = i
            for i in range(7):
                out+=s+(i+1)
                lm+=1
                if lm==n:
                    flag = True
                    break
                
            if flag:
                break
        return out