# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        st = 1
        en = n
        while st<=en:
            mid = (st+en)//2
            if guess(mid)==-1:
                en = mid-1
            elif guess(mid)==1:
                st = mid+1
            else:
                return mid

        