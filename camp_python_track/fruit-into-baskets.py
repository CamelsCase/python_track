class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        st = 0
        en = 0
        freq =  Counter()
        mx = 0
        while st<len(fruits):
            while en<len(fruits) and len(freq)<=2:
                freq[fruits[en]]+=1
                en+=1
            mx = max(mx,en-st-(1 if len(freq)>2 else 0))
            if en==len(fruits):
                break
            while st<len(fruits) and len(freq)>2:
                freq[fruits[st]]-=1
                if freq[fruits[st]]==0:
                    del freq[fruits[st]]
                st+=1
        return mx