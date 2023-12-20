class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left = []
        right = []
        count = 0
        for i in nums:
            if i<pivot:
                left.append(i)
            elif i== pivot:
                count +=1
            elif i>pivot:
                right.append(i)
        for i in range(count):left.append(pivot)
        left.extend(right)
        return left