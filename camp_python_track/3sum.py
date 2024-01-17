from collections import defaultdict

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1

        for i in range(len(nums)-2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            counts[nums[i]] -= 1
            for j in range(i+1, len(nums)-1):
                if nums[i] + nums[j] > 0:
                    break
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                counts[nums[j]] -= 1
                complement = -nums[i] - nums[j]
                if complement in counts and counts[complement] > 0 and complement >= nums[j]:
                    result.add((nums[i], nums[j], complement))
                counts[nums[j]] += 1
            counts[nums[i]] += 1

        return list(result)