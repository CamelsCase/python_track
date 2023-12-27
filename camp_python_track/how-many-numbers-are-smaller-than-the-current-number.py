class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ind = Counter(nums)
        out = []
        seen = dict()
        for i in nums:
            if i not in seen:
                cnt  = 0
                for j,ls in ind.items():
                    if i>j:
                        cnt+=ls
                seen[i]=cnt
            out.append(seen[i])
        return out