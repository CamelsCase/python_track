class BrowserHistory:

    def __init__(self, homepage: str):
        self.ptr = 0
        self.leng = 1
        self.stack = [homepage]
        

    def visit(self, url: str) -> None:
        self.stack = self.stack[:self.ptr+1]
        self.stack.append(url)
        self.ptr+=1
        self.leng = len(self.stack)
        
    def back(self, steps: int) -> str:
        self.ptr =self.ptr-steps
        self.ptr = self.ptr if self.ptr>=0 and self.ptr<self.leng else 0 if self.ptr<0 else self.leng-1
        return self.stack[self.ptr]
        

    def forward(self, steps: int) -> str:
        self.ptr =self.ptr+steps
        self.ptr = self.ptr if self.ptr>=0 and self.ptr<self.leng else 0 if self.ptr<0 else self.leng-1
        return self.stack[self.ptr]



# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)