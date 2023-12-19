class Solution:
    def isPalindrome(self, x: int) -> bool:
        s2 =str(x)
        start =0
        end = -1
        if(len(s2)==1):
            return True
        else:
            for i in range(len(s2)//2):
                if s2[start+i] != s2[end-i]:
                    return False
                
        return True