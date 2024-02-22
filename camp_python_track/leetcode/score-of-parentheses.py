class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack  =[0]
        for i in s:
            if i=="(":
                stack.append(0)
            else:
                top = stack.pop()
                val =max(1,top*2)
                stack[-1] += val
        return stack[-1]