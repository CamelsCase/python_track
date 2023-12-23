class Solution:
    def flipgame(self, fronts: list[int], backs: list[int]) -> int:
        ls = set()
        leng = len(fronts)
        illegal = set()
        for i in range(leng):
            if fronts[i] != backs[i]:
                ls.add(fronts[i])
                ls.add(backs[i])
            else:
                illegal.add(fronts[i])
        x = [i for i in ls if i not in illegal]
        return min(x) if x else 0