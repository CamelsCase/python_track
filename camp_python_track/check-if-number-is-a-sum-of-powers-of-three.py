class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        powers = []
        for i in range(17):
            pw = 3**i
            if pw<=n:
                powers.append(pw)
            else:
                break
        for i in powers[::-1]:
            if i<=n:
                n-=i
        return not bool(n)