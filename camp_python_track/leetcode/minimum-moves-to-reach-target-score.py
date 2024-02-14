class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        cnt = 0
        while target!=1:
            if maxDoubles==0:
                cnt+=target-1
                break
            # print(target,cnt)
            ev = target%2
            target-=ev
            cnt+=ev
            # print(target,cnt)
            if target==1:
                break
            if maxDoubles>0:
                target//=2
                cnt+=1
                maxDoubles-=1
            # print(target,cnt)
        return cnt

