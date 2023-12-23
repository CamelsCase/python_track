class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        start = 0
        end = -1
        leng = len(arr)
        while start < leng-1 and arr[start] < arr[start+1]: start += 1
        while end > -leng and arr[end] < arr[end-1]:end -= 1
        return start == end + leng and 0 < start and end < -1