class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        self.ans = []
        vote  = defaultdict(int)
        cur_winner = None
        for i in range(len(persons)):
            vote[persons[i]]+=1
            if cur_winner==None:
                cur_winner = persons[i]
            else:
                if vote[persons[i]]>=vote[cur_winner]:
                    cur_winner = persons[i]
            self.ans.append(cur_winner)
            

    def q(self, t: int) -> int:
        ind = bisect_right(self.times,t)-1
        return self.ans[ind]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)