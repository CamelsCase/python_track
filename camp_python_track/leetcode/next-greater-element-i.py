class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greater = {} 
        mx = -1
        for i in nums2:
            if not stack:
                stack.append(i)
            else:
                if stack[-1]>i:
                    stack.append(i)
                else:
                    while stack and stack[-1]<i:
                        next_greater[stack.pop()] = i
                    stack.append(i)
        out = []
        for i in nums1:
            if i in stack:
                out.append(-1)
            else:
                out.append(next_greater[i])
        return out

                    
        