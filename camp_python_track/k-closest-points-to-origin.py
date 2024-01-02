class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closest = []
        for point in points:
            distance = sqrt(point[0] ** 2 + point[1] ** 2)
            closest.append((distance, point))
        closest.sort(key=lambda x: x[0])
        out = [point for _, point in closest[:k]]
        return out
