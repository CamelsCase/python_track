class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        wall_set = {(i, j) for i, j in walls}
        guards = {(i, j) for i, j in guards}
        guarded_points = set()
        len_guards = 0
        len_guarded_points = 0
        for x, y in guards:
            len_guards+=1
            # Going upward
            for i in range(x - 1, -1, -1):
                if (i, y) in wall_set or (i, y) in guards:
                    break
                if  (i, y) in guarded_points:
                    continue
                else:
                    guarded_points.add((i, y))
                    len_guarded_points+=1

            # Going downward
            for i in range(x + 1, m):
                if (i, y) in wall_set or (i, y) in guards:
                    break
                if  (i, y) in guarded_points:
                    continue
                else:
                    guarded_points.add((i, y))
                    len_guarded_points+=1

            # Going left
            for i in range(y - 1, -1, -1):
                if (x, i) in wall_set or (x, i) in guards:
                    break
                if  (x, i) in guarded_points:
                    continue
                else:
                    guarded_points.add((x, i))
                    len_guarded_points+=1

            # Going right
            for i in range(y + 1, n):
                if (x, i) in wall_set or (x, i) in guards:
                    break
                if  (x, i) in guarded_points:
                    continue
                else:
                    guarded_points.add((x, i))
                    len_guarded_points+=1

        total_grids = n * m
        tot_guarded = len_guards + len(wall_set) + len_guarded_points
        return total_grids - tot_guarded