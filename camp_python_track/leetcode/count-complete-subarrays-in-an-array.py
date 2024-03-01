class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        uniq = set(nums)
        def complete(uniq,have):
            if uniq==have:
                return True
            return False
        st = 0
        en = 0
        freq = Counter()
        cnt = 0
        leng =  len(nums)
        while st<leng and en<leng:
            while en<leng and not complete(uniq,set(freq.keys())):
                freq[nums[en]]+=1
                en+=1
            if st==en:
                break
            while st<en and  complete(uniq,set(freq.keys())):
                cnt+=leng-en+1
                freq[nums[st]]-=1
                if freq[nums[st]]==0:
                    del freq[nums[st]]
                st+=1
        return cnt