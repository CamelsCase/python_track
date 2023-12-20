
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        commons = set(list1).intersection(set(list2))
        x  = dict()
        for i in commons:
            x[i]=list1.index(i)+list2.index(i)
        mn = min(x.values())
        out = []
        for i in x:
            if x[i]==mn:
                out.append(i)
        return out
        