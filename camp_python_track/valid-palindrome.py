def rec(n,start,end):
    if len(n)<=1:
        return True
    if n[start]!=n[end]:
        return False
    if start>=end:
        return True
    return rec(n,start+1,end-1)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        ls = []
        for i in s:
            if i.isalnum():
                ls.append(i.lower())
        s = "".join(ls)
        print(s)
        leng = len(s)
        return rec(s,0,leng-1)