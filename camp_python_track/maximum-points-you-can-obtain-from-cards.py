class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        leng = len(cardPoints)
        window = leng-k
        prev = sum(cardPoints[:window])
        mn = prev
        for i in range(1,k+1):
            prev +=  (cardPoints[i+window-1]-cardPoints[i-1])           
            if prev<mn:
                mn = prev
        return sum(cardPoints)-mn



            
