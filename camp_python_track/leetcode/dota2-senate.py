class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        freq = Counter(senate)
        if len(freq)<2:
            if "R" in freq:
                return "Radiant"
            return "Dire"
        ban_dire = 0
        ban_radient = 0
        q = deque()
        q.extend(senate)
        while len(freq)>1:
            turn = q.popleft()
            if turn=="R":
                if ban_radient==0:
                    freq["D"]-=1
                    if freq["D"]==0:
                        del freq["D"]
                        return "Radiant"
                    ban_dire+=1
                    q.append(turn)
                else:
                    ban_radient-=1
            else:
                if ban_dire==0:
                    freq["R"]-=1
                    if freq["R"]==0:
                        del freq["R"]
                        return "Dire"
                    ban_radient+=1
                    q.append(turn)
                else:
                    ban_dire-=1

        