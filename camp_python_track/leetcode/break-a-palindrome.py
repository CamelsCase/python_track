class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        # freq = Counter(palindrome)
        if len(palindrome)==1:
            return ""
        for i in range(len(palindrome)//2):
                if 97-ord(palindrome[i])!=0:
                    return palindrome[:i]+"a"+palindrome[i+1:]
        return palindrome[:-1]+"b"

                

                
                





