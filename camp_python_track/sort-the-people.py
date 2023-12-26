class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        mp =[]
        for i in range(len(names)):
            mp.append([names[i],heights[i]])
        mp.sort(key=lambda x:x[1],reverse=True)
        return [i[0] for i in mp]
