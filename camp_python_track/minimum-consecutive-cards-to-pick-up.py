class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        freq = Counter()
        st = 0
        en = 0
        mn = len(cards)+1
        while st<len(cards):
            while en<len(cards) and freq[cards[en]]<1:
                freq[cards[en]]+=1
                en+=1
            if en==len(cards):
                break
            while st<len(cards) and freq[cards[en]]>=1:
                freq[cards[st]]-=1
                st+=1
            mn = min(mn,en-st+2)
        return mn if mn<len(cards)+1 else -1