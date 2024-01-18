class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        s = 0
        opposite = "B" if blocks[-1]=="W" else "W"
        blocks+=opposite
        blacks = blocks[s:s+k].count("B")
        mn = k
        whites = k-blacks
        if k==len(blocks):
            return whites
        while s+k<len(blocks):
            if whites<mn:
                mn = whites
            if blocks[s+k] != blocks[s]:
                if blocks[s]=="W":
                    whites-=1
                    blacks+=1
                else:
                    blacks-=1
                    whites+=1
            s+=1
        return mn