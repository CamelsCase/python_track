class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        leng = len(weights)
        def how_many_days(capacity):#this functions will find the number of days we need to ship all the weights if we have capacity equal to capacity
            nonlocal leng
            the_days = 0
            sm = 0
            for i in range(leng):
                if sm+weights[i]<=capacity:
                    sm+=weights[i]
                else:
                    the_days+=1
                    sm = weights[i]
            return the_days+1

        left = max(weights)
        right = sum(weights)

        best_till_now = right

        while left<=right:
            mid = left+(right-left)//2
            if how_many_days(mid)<=days:
                if mid<best_till_now:
                    best_till_now = mid
            if how_many_days(mid)>days:
                left=mid+1
            elif how_many_days(mid)<=days:
                right = mid-1
        return best_till_now
            
        