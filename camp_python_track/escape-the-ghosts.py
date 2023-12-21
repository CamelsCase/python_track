class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        ghosts_time = []
        for i in ghosts:
            vd = abs(i[1]-target[1])
            hd = abs(i[0]-target[0])
            ghosts_time.append(vd+hd)
        print(ghosts_time)
        sm = abs(target[0])+abs(target[1])
        return sm<min(ghosts_time)