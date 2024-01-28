class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()  
        closest_sum = float('inf') 
        size = len(nums)
        for i in range(size - 2):  
            left = i + 1  
            right = size - 1 
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right] 
                if current_sum == target:
                    return current_sum  
                if abs(target - current_sum) < abs(target - closest_sum):
                    closest_sum = current_sum
                if current_sum < target:
                    left += 1  
                else:
                    right -= 1 
        return closest_sum 