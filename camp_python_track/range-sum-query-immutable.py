class NumArray:

    def __init__(self, nums: list[int]):
        self.nums =nums
        for i in range(1, len(self.nums)): 
            self.nums[i] = self.nums[i - 1] + self.nums[i] 

    def sumRange(self, left: int, right: int) -> int:
        return self.nums[right]-(self.nums[left-1]if left>0 else 0)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(self.nums)
# param_1 = obj.sumRange(left,right)