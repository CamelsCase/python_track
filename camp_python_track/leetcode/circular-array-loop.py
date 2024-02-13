class Solution:
    def check(self,start,nums,computed,go):
        seen = set()
        sim = -1 if nums[start]<0 else 1
        dir = start
        found = True
        while dir not in seen:
            if dir in computed:
                return computed[dir]
            seen.add(dir)
            dir = go[dir]
            if sim*nums[dir]<0:
                found = False
                break
        leng = 0
        if found:
            seen_leng = set()
            while dir not in seen_leng:
                leng+=1
                seen_leng.add(dir)
                dir = go[dir]
        if found and leng>1:
            computed[start] = True
            return True
        computed[start] = False
        return False

    def circularArrayLoop(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return False
        go = {}
        for i in range(len(nums)):
            if nums[i]>0:
                go[i] =(i+nums[i])%len(nums)
            else:
                mv = i+nums[i]
                if mv<0:
                    mv = -(abs(mv)%len(nums))
                    mv=len(nums)+mv
                go[i] = mv
        print(go)
        computed = {}
        for i in range(len(nums)):
            if self.check(i,nums,computed,go):
                return True
        return False

        