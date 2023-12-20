class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        negs = [i  for i in nums if i<0]
        poss = [i  for i in nums if i>0]
        out = []
        ind = 0
        for _ in negs:
            out.append(poss[ind])
            out.append(negs[ind])
            ind+=1
        return out