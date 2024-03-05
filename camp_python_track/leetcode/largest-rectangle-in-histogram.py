class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        _max = 0
        length = len(heights)
        for i in range(length):
            index = i
            while stack and heights[i]<stack[-1][0]:
                removed = stack.pop()
                index = removed[1]
                _max = max(_max,removed[0]*(i-removed[1]))
            stack.append((heights[i],index))
        while stack:
            new_removed = stack.pop()
            _max = max(_max,new_removed[0]*(length-new_removed[1]))
        return _max