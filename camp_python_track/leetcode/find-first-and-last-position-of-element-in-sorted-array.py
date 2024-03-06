class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        fst,lst = 0,0
        fen,le = len(nums)-1,len(nums)-1
        ft = [-1,-1]
        while fst<=fen or lst<=le:
            fmid = fst+(fen-fst)//2
            lmid = lst+(le-lst)//2

            if fst<=fen:
                if target<=nums[fmid]:
                    if nums[fmid]==target:
                        ft[0] = fmid
                    fen = fmid-1
                elif  target>nums[fmid]:
                    fst = fmid+1

            if lst<=le:
                if target<nums[lmid]:
                    le = lmid-1
                elif  target>=nums[lmid]:
                    if nums[lmid]==target:
                        ft[1] = lmid
                    lst = lmid+1
        # print(ft)
        return ft


        