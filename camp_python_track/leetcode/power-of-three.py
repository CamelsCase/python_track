class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while True:
            if n==0:
                return False
            elif n==3 or n==1:
                return True
            elif n%3 ==0:
                n/=3
            else:
                return False