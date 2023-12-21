class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        sm = sum([i for i in nums if abs(i)%2==0 ])
        out = []
        for val,ind in queries:
            if abs(nums[ind])%2==0:
                if abs(nums[ind]+val)%2==0:
                        sm += val
                else:
                    sm -= nums[ind]
            else:
                if abs(nums[ind]+val)%2==0:
                    sm += (nums[ind]+val)
            nums[ind]+= val 
            out.append(sm)
        return out  