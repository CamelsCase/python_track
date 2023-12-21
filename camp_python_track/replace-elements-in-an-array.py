class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        # ind = {nums[i]:i for i in range(len(nums))}
        # for i in operations:
        #     index = ind[i[0]]
        #     del ind[i[0]]
        #     ind[i[1]] = index
        # return  [i[0] for i in sorted(ind.items(), key=lambda x: x[1])]
        ind = {nums[i]:i for i in range(len(nums))}
        for i in operations:
            index = ind[i[0]]
            del ind[i[0]]
            ind[i[1]] = index
        for val,ind in ind.items():
            nums[ind]=val
        return  nums