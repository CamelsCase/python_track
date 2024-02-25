class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        q = deque()
        q.append(deck[-1])
        for i in range(len(deck)-2,-1,-1):
            q.appendleft(q.pop())
            q.appendleft(deck[i])
        return q
            

        