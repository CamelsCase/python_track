class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def lesser(dt1,dt2):
            for i in dt2:
                if dt1[i]<dt2[i]:
                    return True
            return False
        st = 0
        en = 0
        chars = Counter()
        dt = Counter(t)
        if dt==chars:
            return s[:len(t)]
        leng = len(s)
        mn = [leng,""]
        while st<leng and en<leng:
            while en<leng and lesser(chars,dt):
                if s[en] in dt:
                    chars[s[en]]+=1
                en+=1
            while not lesser(chars,dt) and st<leng:
                if mn[0]>=en-st:
                    mn = [en-st,s[st:en]]
                if s[st] in dt:
                    chars[s[st]]-=1
                if chars[s[st]]==0:
                    del chars[s[st]]
                st+=1
        return mn[1]