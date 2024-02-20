class Solution:
    cnt = 0
    def reverseString(self, s: List[str]) -> None:
        st,en = 0+self.cnt,len(s)-self.cnt-1
        if st>=en:
            return None
        s[st],s[en] = s[en],s[st]
        self.cnt+=1
        self.reverseString(s)
       