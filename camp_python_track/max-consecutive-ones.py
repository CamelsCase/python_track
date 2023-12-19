class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ones = []
        cons = 0
        for i in nums:
            if i ==1:
                cons+=1
            else:
                ones.append(cons)
                cons=0
        ones.append(cons)
        return max(ones)