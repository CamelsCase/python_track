class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        q = deque()
        q.extend([i,tickets[i]] for i in range(len(tickets)))
        time_needed = 0
        while q and not (q[0][0]==k and q[0][1]==0):
            # print(q,k,time_needed)
            val = q.popleft()
            if val[1]>0:
                time_needed+=1
                val[1]-=1
                if val[1]==0:
                    if val[0]==k:
                        break
                else:
                    q.append(val)

        
        return time_needed