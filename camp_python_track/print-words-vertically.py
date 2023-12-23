class Solution:
    def printVertically(self, s: str) -> List[str]:
        ls = s.split()
        leng = len(ls)
        mx = max(ls,key=len)
        print(mx)
        mx= len(mx)
        for i in range(leng):
            if len(ls[i])<mx:
                ls[i]+=(mx-len(ls[i]))*' '
        print(mx)
        cnt = 0
        out = []
        for element in range(mx):
            ot = ""
            for ind in range(leng):
                ot+=ls[ind][cnt]
            
            cnt+=1
            out.append(ot.rstrip())
        return out