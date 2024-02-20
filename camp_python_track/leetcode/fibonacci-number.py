class Solution:
    def fib(self, n: int) -> int:
        out = 0
        if n<=1:
            return n
        fprev,fcurr = 0,1
        # fcurr = 1
        for i in range(2,n+1):
            out=fprev+fcurr
            fprev = fcurr
            fcurr = out
        return out