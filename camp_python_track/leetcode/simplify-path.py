class Solution:
    def simplifyPath(self, path: str) -> str:
        
        ls = path.split("/")
        stack = []
        print(ls)
        for i in ls:
            if i=="" or i==".":
                continue
            elif i=="..":
                if stack:
                    stack.pop()
            else:
                stack.append(i)
        ans = "/".join(stack)
        return "/" +ans

