class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        fr1 = Counter(nums1)
        fr2 = Counter(nums2)
        out = []
        for i in set(nums1).intersection(nums2):
            for _ in range(min(fr1[i],fr2[i])):
                out.append(i)
        return out
