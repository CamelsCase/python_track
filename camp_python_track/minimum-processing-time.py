class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse=True)
        mx = 0
        ind = 0
        for i in processorTime:
            mx = max(mx,i+tasks[ind])
            ind+=4
        return mx