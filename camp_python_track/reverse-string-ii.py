class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        n = len(s)
        res = ''
        i = 0
        while i < n:
            if i + k <= n:
                res += s[i:i+k][::-1]
                res += s[i+k:i+2*k]
            else:
                res += s[i:][::-1]
            i += 2*k
        return res