class Solution:
    def balancedString(self, s: str) -> int:
        def lesser(dc1 ,dc2):
            for i in dc2:
                if dc1[i]<dc2[i]:
                    return True
            return False
        leng = len(s)
        allowed = leng//4
        freq = Counter(s)-Counter("Q"*allowed+"W"*allowed+"E"*allowed+"R"*allowed)
        st = 0
        en = 0
        check = Counter()
        mn = leng
        while st<leng and en<leng:
            while en<leng and lesser(check,freq):
                # print(freq)
                # print(check)
                # print(st,en,mn)
                if s[en] in freq:
                    check[s[en]]+=1
                en+=1
            if st==en:
                mn = min(mn,en-st)
                break
            while st<en and not lesser(check,freq):
                # print(freq)
                # print(check)
                # print(st,en,mn)
                mn = min(mn,en-st)
                if s[st] in freq:
                    check[s[st]]-=1

                st+=1
        return mn

                