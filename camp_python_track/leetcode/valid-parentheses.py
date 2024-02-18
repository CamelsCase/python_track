class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairing = {"(":")","[":"]","{":"}"}
        for i in s:
            if i in "([{":
                stack.append(i)
            else:
                if not stack:
                    return False
                if pairing[stack[-1]]!=i:
                    return False
                else:
                    stack.pop()

        return len(stack)==0

        