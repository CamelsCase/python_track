class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def is_nice(substring):
            char_set = set(substring)
            for char in substring:
                if char.swapcase() not in char_set:
                    return False
            return True

        n = len(s)
        longest = ""

        for i in range(n):
            for j in range(i + len(longest), n):
                substring = s[i:j+1]
                if is_nice(substring) and len(substring) > len(longest):
                    longest = substring

        return longest