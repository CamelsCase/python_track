class Solution:
    def bestClosingTime(self, customers: str) -> int:
        cs = [1 if i=="Y" else 0 for i in customers]
        leng = len(customers)
        y = [0]*(leng+1)
        n = [0]*(leng+1)
        for i in range(leng):
            y[i+1]=y[i]+(cs[leng-i-1])
            n[i+1]=n[i]+(1-cs[i])
        mx = ind = leng
        for i in range(leng+1):
            if n[i]+y[leng-i]<mx:
                mx = n[i]+y[leng-i]
                ind = i
        return ind
        #time complexity O(N)
        #space complexity O(N)