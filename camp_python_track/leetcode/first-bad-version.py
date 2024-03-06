# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        best = None
        def find(st,en):
            nonlocal best
            mid = st+(en-st)//2
            # print(st,mid,en)
            if not isBadVersion(mid):
                st = mid+1
            if isBadVersion(mid):
                best = mid
                en = mid-1
            if st>en:
                return best
            find(st,en)
            return best
        return find(1,n)
            