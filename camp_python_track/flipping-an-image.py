class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        return [[0 if j==1 else 1 for j in i[::-1]] for i in image]

