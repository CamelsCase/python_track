class Solution:
    def rec(self,n,s):
        if n==0:
            return ""
        n-=1
        return s+self.rec(n,s)            
    def decodeString(self, s: str) -> str:
        stack = []
        for i in s:
            if i!="]":
                stack.append(i)
            else:
                val = []
                while stack and not stack[-1].isdigit():
                    ch = stack.pop()
                    if ch!="[":
                        val.append(ch)
                times = []
                while stack and stack[-1].isdigit():
                    times.append(stack.pop())
                times = int("".join(times[::-1]))
                n = "".join(val[::-1])
                stack.append(self.rec(times,n))
        out = []
        for i in stack:
            out.append(i)
        return "".join(out)
        
        
            
