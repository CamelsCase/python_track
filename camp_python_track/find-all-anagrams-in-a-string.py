class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        desired_freq = Counter(p)
        freq = Counter(s[:len(p)])
        out = []
        if freq==desired_freq:
                out.append(0)
        for i in range(len(s)-len(p)):
            freq[s[i]]-=1
            if freq[s[i]]==0:
                del freq[s[i]]
            freq[s[i+len(p)]]+=1
            if freq==desired_freq:
                    out.append(i+1)
        return out

        