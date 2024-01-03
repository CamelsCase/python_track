class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        pt1 = 0
        pt2 = 0
        leng1 = len(nums1)
        leng2 = len(nums2)
        try:
            while pt1<leng1 and pt2<leng2 and nums1[pt1]!=nums2[pt2]:
                if nums1[pt1]>nums2[pt2]:
                    pt2+=1
                else:
                    pt1+=1
            return nums1[pt1] if nums1[pt1]==nums2[pt2] else -1
        except Exception:
            return -1
        
        