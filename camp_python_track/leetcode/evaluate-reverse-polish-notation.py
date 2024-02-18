class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i not in "+-*/":
                stack.append(i)
            else:
                first = stack.pop()
                second = stack.pop()
                if i== "+":
                    stack.append(str(eval(f"{second}+{first}")))
                elif i== "-":
                    stack.append(str(eval(f"{second}-{first}")))
                elif i== "*":
                    stack.append(str(eval(f"{second}*{first}")))
                elif i== "/":
                    stack.append(str(int(eval(f"{second}/{first}"))))
        return int(stack[0])
