class Solution:
    ans  =1
    def countGoodNumbers(self, n: int) -> int:
        if n%2==0:
            val = n//2
        else:
            val=n//2+1
        p1 = pow(5,val,10**9+7)
        p2 = pow(4,n-val,10**9+7)
        return (p1*p2)%(10**9+7)
        