class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l , r = 0, len(arr)-k
        
        while l < r:
            middle = (r+l) // 2
            if arr[middle+k] <= x:
                l = middle + 1
            else:
                left_dist_mid = abs(x-arr[middle])
                right_dist_mid = abs(x-arr[middle+k])
                
                if left_dist_mid <= right_dist_mid:
                    r = middle
                else:
                    l = middle + 1
        return arr[l:l+k]
        
                