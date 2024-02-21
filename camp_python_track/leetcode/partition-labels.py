class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dt = {ch:ind for ind,ch in enumerate(s)}
        prev = anchor = 0
        ls = []
        for i in range(len(s)):
            anchor = max(dt[s[i]],anchor)  
            if anchor==i: 
                ls.append(anchor-prev+1)
                prev= anchor+1
        return ls
             