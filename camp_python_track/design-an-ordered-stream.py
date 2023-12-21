class OrderedStream:

    def __init__(self, n: int):
        self.ind = 1
        self.hashmap = dict()
        

    def insert(self, idKey: int, value: str) -> List[str]:
        self.hashmap[idKey] = value
        out = []
        if idKey>self.ind:
            return out
        while idKey in self.hashmap:
            out.append(self.hashmap[idKey])
            idKey += 1
            self.ind = idKey
            
        return out
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)