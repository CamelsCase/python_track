class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        out = []
        if arr==sorted(arr):
            return out
        for i in range(len(arr)-1,-1,-1):
            ind = arr.index(i+1)
            if ind!=i:
                out.append(ind+1)
                arr[:ind+1] = arr[:ind+1][::-1]
                out.append(i+1)
                arr[:i+1] = arr[:i+1][::-1]
        return out