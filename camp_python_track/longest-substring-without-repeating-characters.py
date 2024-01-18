class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = Counter()
        right = 0
        left = 0
        mx=0
        while right<len(s):
            freq[s[right]]+=1
            mx = max(mx,right-left)
            while left<=right<len(s) and freq[s[right]]>1:
                freq[s[left]]-=1
                left+=1
            right+=1
        mx = max(mx,right-left)
        return mx