class Solution:
    def myPow(self, x: float, n: int) -> float:

        def solve(x, n):
            if x == 0: 
                return 0
            if n == 0: 
                return 1
            ans = solve(x*x, n//2)
            return ans*x if n%2 else ans
        ans = solve(x, abs(n))
        return ans if n >= 0 else 1/ans
        