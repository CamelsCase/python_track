class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        changes = {5:0,10:0,20:0}
        for ind,i in enumerate(bills):
            want = i-5
            if want==0:
                changes[i]+=1
            else:
                if want>=10 and changes[10]>0:
                    allowedTen = min(changes[10],want//10)
                    want-=allowedTen*10
                    changes[10]-=allowedTen
                if want>0:
                    allowedFive = min(changes[5],want//5)
                    if changes[5]>0:
                        want-=allowedFive*5
                        changes[5]-=allowedFive
                if want!=0:
                    return False
                changes[i]+=1
        return True