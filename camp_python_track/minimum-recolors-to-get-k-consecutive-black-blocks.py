class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        freq = Counter(blocks[:k])
        st =0
        en = k
        mn = freq["W"]
        while en<len(blocks):
            freq[blocks[en]]+=1
            freq[blocks[st]]-=1
            mn = min(mn,freq["W"])
            st+=1
            en+=1
        return mn