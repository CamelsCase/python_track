class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        d = deque()
        leng = len(nums)
        nums.extend(nums)
        next_greater = defaultdict(lambda:-1)
        for i in range(leng*2):
            while d and d[-1][1]<nums[i]:
                val = d.pop()
                next_greater[val[0]%leng]=i%leng
            d.append((i%leng,nums[i]))
            # print(d)
            # print(next_greater)
        out = []
        for i in range(leng):
            ind  =next_greater[i]
            out.append(nums[ind] if ind>=0 else -1)
        return out















































        