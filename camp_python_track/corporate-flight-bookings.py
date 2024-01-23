class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        flights = [0]*(n+1)
        for i in bookings:
            flights[i[0]-1]+=i[2]
            flights[i[1]]-=i[2]
        pre = list(accumulate(flights))
        return pre[:-1]