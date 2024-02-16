class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        pair = {"{":"}","[":"]","(":")"}
        stack  =[]
        fault = 0
        for i in s:
            if i in pair.keys():
                stack.append(i)
            else:
                if stack and pair[stack[-1]]==i:
                    stack.pop()
                else:
                    fault+=1
        return fault+len(stack)
        