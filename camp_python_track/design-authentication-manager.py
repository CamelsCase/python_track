class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.auth  = dict()
        
    def generate(self, tokenId: str, currentTime: int) -> None:
        self.auth[tokenId]=currentTime
        
    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.auth:
            if self.auth[tokenId]+self.timeToLive>currentTime:
                self.auth[tokenId] = currentTime
                
    def countUnexpiredTokens(self, currentTime: int) -> int:
        cnt = 0
        for i in self.auth.keys():
            if self.auth[i]+self.timeToLive>currentTime:
                cnt+=1
        return cnt
        
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)