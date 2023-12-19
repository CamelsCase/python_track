class Solution:
    def largestGoodInteger(self, num: str) -> str:
        mx = None
        freq = Counter(num[:3])
        for i in range(3,len(num)):
            if len(freq.keys())==1:
                if not mx:
                    mx =list(freq.keys())[0]*3
                else:
                    mx = max(mx,list(freq.keys())[0]*3)
            freq[num[i-3]]-=1
            freq[num[i]]+=1
            if freq[num[i-3]]==0:
                del freq[num[i-3]]
        if len(freq.keys())==1:
                if not mx:
                    mx =list(freq.keys())[0]*3
                else:
                    mx = max(mx,list(freq.keys())[0]*3)
        out = mx*3 if mx ==0 else "" if not mx else mx
        return  out
            

