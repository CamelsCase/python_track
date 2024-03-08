class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []
        for i in s:
            if i=="]":
                q = deque()
                while stack and stack[-1]!="[":
                    q.appendleft(stack.pop())
                stack.pop()
                x = deque()
                while stack and stack[-1].isdigit():
                    x.appendleft(stack.pop())
                word = "".join(q)
                mult = int("".join(x))
                stack.append(word*mult)
            else:
                stack.append(i)
        return "".join(stack)

                