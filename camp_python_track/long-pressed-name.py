class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        p1 = 0
        p2 = 0
        prev = None
        prev = None
        while p1<len(name) and p2<len(typed) :
            if name[p1]==typed[p2]:
                prev = name[p1]
                p2+=1
                p1+=1
            while p1<len(name) and p2<len(typed) and name[p1]!=typed[p2]:
                if prev==typed[p2]:
                    p2+=1
                else:
                    return False
        while p2<len(typed) and  prev==typed[p2]:
            p2+=1
        return True if p1==len(name) and p2==len(typed) else False