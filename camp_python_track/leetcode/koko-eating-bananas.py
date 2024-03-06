class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def how_many_hours(speed):
            hours = 0
            for i in piles:
                hours += math.ceil(i / speed)
            return int(hours) <= h
        left = 1
        right = max(piles)

        while left <= right:
            mid = (left + right)//2
            if how_many_hours(mid):
                right = mid -1
            else:
                left = mid + 1
        return left