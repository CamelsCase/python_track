class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        s=""
        out = []
        for i in range(len(nums)):
            if i%2 == 0:
                s+= (str(nums[i+1])+ " ")*nums[i]
        for i in s.split():
            print(i)
            out.append(int(i))
        return out