class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        leng = len(nums)
        if leng<3:
            return list(set(nums))
        out = set()
        freq = Counter(nums).most_common()
        requirement = leng/3
        if freq[0][1]<=requirement:
            return []
        else:
            for num,count in freq:
                if count>requirement:
                    out.add(num)
        return list(out)