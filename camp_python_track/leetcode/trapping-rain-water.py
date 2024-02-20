class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = [0]*len(height)
        right_max = [0]*len(height)
        left_max[0] = height[0]
        right_max[-1]= height[-1]
        leng = len(height)-1
        for i in range(1,len(height)):
            left_max[i] = max(left_max[i-1],height[i])
            right_max[leng-i] = max(right_max[leng-i+1],height[leng-i])
        print(left_max)
        print(right_max)
        out = 0
        for i in range(leng+1):
            out+=max(min(left_max[i],right_max[i])-height[i],0)
        return out




        